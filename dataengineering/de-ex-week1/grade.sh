cp ./compare_files.sh $1/compare_files.sh
cp ./solution_output.csv $1/solution_output.csv
cp ./orders.csv $1/orders.csv
cp ./users.csv $1/users.csv
cd $1

if [ -e prepare.sh ]; then
    echo "Detected prepare.sh script"
    ./prepare.sh
fi

if [ ! -e wtc_week1.ipynb ]; then
    echo "wtc_week1.ipynb was not found"
    exit 1
fi

#Execute notebook
jupyter execute wtc_week1.ipynb

#compare output CSV file
./compare_files.sh solution_output.csv output.csv