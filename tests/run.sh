clear
cd test
python3 create_baseline.py
# exit 0
cd ..
python test/setup.py &&
	pytest test/test_centrality.py
	# pytest
