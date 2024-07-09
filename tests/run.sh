clear
python3 test/setup.py &&
  python3 test/baseline/create_baselines.py &&
  pytest test/test_centrality.py test/test_ml.py
