clear
python3 test/create_baseline.py &&
  python3 test/setup.py &&
  pytest test/test_centrality.py::TestCentrality
# pytest
