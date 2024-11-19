mkdir -p $1/tests
cp tests/test_anagrams.py $1/tests
cp tests/hamlet.txt $1/tests
cd $1
python3 -m pytest -v