mkdir -p $1/tests
cp tests/test_ttt.py $1/tests
cd $1
python3 -m pytest -v