clear
cd data
python3 create_baseline.py
cd ..
python test/setup.py &&
	pytest
