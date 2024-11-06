cd $1

echo "Removing old output files in dir $1"

file1="local_sqlite_database.db"

if [ -f "$file" ]; then
    echo "File $file exists. Deleting..."
    rm "$file"
    if [ $? -eq 0 ]; then
        echo "File $file has been successfully deleted."
    else
        echo "Failed to delete $file."
    fi
else
    echo "File $file does not exist."
fi

