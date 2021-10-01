#include <vector>
#include <algorithm>


  bool updateCount(const HeapAccum& heap, double incoming_similarity, int k) {
    std::vector<double> scores;
    for (auto a : heap.data_)
      scores.push_back(a.similarity);
    
    if (scores.size() < k)
      return 1;
    
    scores.push_back(incoming_similarity);
    std::make_heap(std::begin(scores), std::end(scores));
    std::sort_heap(std::begin(scores), std::end(scores));
    return (incoming_similarity == scores[0]) ? 0 : 1;
  }
