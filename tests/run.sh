clear
cd data
python3 create_baseline.py
cd ..
# python test/setup.py &&
# pytest test/test_centrality.py::TestCentrality::test_degree_centrality4
pytest test/test_centrality.py::TestCentrality::test_degree_centrality2
# pytest test/test_centrality.py
	# pytest
# pytest --junitxml "output.xml" #-n 4
