clear
python3 test/setup.py &&
  # python3 test/baseline/create_baselines.py &&
  # pytest test/test_centrality.py::TestCentrality::test_degree_centrality1 #test/test_ml.py
  pytest test/test_centrality.py::TestCentrality::test_pagerank
  # pytest test/test_ml.py
echo 'done' 
