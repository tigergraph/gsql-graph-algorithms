
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:34:21 2019
@author: jinhe
"""

import numpy as np
import pandas as pd
from collections import defaultdict
from six import iteritems
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.utils import shuffle as skshuffle
from sklearn.preprocessing import MultiLabelBinarizer
from scipy.sparse import coo_matrix


# define OneVsRest classifer
class TopKRanker(OneVsRestClassifier):
    def predict(self, X, top_k_list):
        assert X.shape[0] == len(top_k_list)
        probs = np.asarray(super(TopKRanker, self).predict_proba(X))
        all_labels = []
        for i, k in enumerate(top_k_list):
            probs_ = probs[i, :]
            labels = self.classes_[probs_.argsort()[-k:]].tolist()
            all_labels.append(labels)
        return all_labels



# read ground truth file and embedding file
label = pd.read_csv("BlogCatalog-dataset 2/data/group-edges.csv","r",delimiter = ",", header = None);
label.columns = ["blog","class"];
embedding =pd.read_csv("Results/Blog/vectors_randomWalk_blog_0724.txt","r", delimiter = " ", header = None);

list_index = embedding[0].tolist()

embedding = embedding.drop(columns = 0)

embedding_list = embedding.values.tolist()

label['class'] = label['class'].apply(lambda x: x-1)

label_dict = label.groupby('blog')['class'].apply(list).to_dict();

label_list = [];
for i in list_index:
    label_list.append(label_dict[i])

label_np = MultiLabelBinarizer().fit_transform(label_list)


data = pd.DataFrame({'embedding':embedding_list})

data['source'] = list_index;
data['label'] = label_list;

features_matrix = np.asarray(embedding);
labels_matrix = coo_matrix(label_np);
labels_count = labels_matrix.shape[1]
mlb = MultiLabelBinarizer(range(labels_count))
shuffles = []
for x in range(10):
    shuffles.append(skshuffle(features_matrix, labels_matrix))

all_results = defaultdict(list)


# define training percentage
training_percents = [0.9]
#training_percents = np.asarray(range(1, 10)) * .1;
for train_percent in training_percents:
    for shuf in shuffles:
        X, y = shuf
        training_size = int(train_percent * X.shape[0])
        X_train = X[:training_size, :]
        y_train_ = y[:training_size]
  
        y_train = [[] for x in range(y_train_.shape[0])]       


        cy =  y_train_.tocoo()
        for i, j in zip(cy.row, cy.col):
            y_train[i].append(j)
  
        assert sum(len(l) for l in y_train) == y_train_.nnz
  
        X_test = X[training_size:, :]
        y_test_ = y[training_size:]
  
        y_test = [[] for _ in range(y_test_.shape[0])]
  
        cy =  y_test_.tocoo()
        for i, j in zip(cy.row, cy.col):
            y_test[i].append(j)
  
        clf = TopKRanker(LogisticRegression())
        clf.fit(X_train, y_train_)
  
        # find out how many labels should be predicted
        top_k_list = [len(l) for l in y_test]
        preds = clf.predict(X_test, top_k_list)
  
        results = {}
        averages = ["micro", "macro"]
        for average in averages:
            results[average] = f1_score(mlb.fit_transform(y_test), mlb.fit_transform(preds), average=average)
  
        all_results[train_percent].append(results)
print ('Results, using embeddings of dimensionality', X.shape[1])
print ('-------------------')


for train_percent in sorted(all_results.keys()):
    print ('Train percent:', train_percent)
    for index, result in enumerate(all_results[train_percent]):
      print ('Shuffle #%d:   ' % (index + 1), result)
    avg_score = defaultdict(float)
    for score_dict in all_results[train_percent]:
      for metric, score in iteritems(score_dict):
        avg_score[metric] += score
    for metric in avg_score:
      avg_score[metric] /= len(all_results[train_percent])
    print ('Average score:', dict(avg_score))
    print ('-------------------')


