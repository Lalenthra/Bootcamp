cp ./solution.dump $1/solution.dump
cd $1

echo "Comparing output in dir $1"

file1="local_sqlite_database.db"
file2="solution.dump"

# Check if both files exist
if [ ! -f "$file1" ]; then
    echo "Error: File $file1 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

if [ ! -f "$file2" ]; then
    echo "Error: File $file2 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

# Expected number of entries in the matching table(s)
expected_count=9

table_pattern="^sales_aggregated_[0-9]{8}$"
# List tables, split into lines, and match each line against the pattern
matching_tables=$(sqlite3 "$file1" ".tables" | tr ' ' '\n' | grep -E "$table_pattern")

# Check if any matching table is found
if [ -z "$matching_tables" ]; then
    echo "No tables found matching pattern '$table_pattern'."
    exit 1
fi

# Loop through each matching table to check the row count
echo "$matching_tables" | while IFS= read -r table; do
    # Get the actual row count for the table
    row_count=$(sqlite3 "$file1" "SELECT COUNT(*) FROM $table;")

    # Check if the row count meets the expected count
    if [ "$row_count" -eq "$expected_count" ]; then
        echo "Table '$table' has the expected number of entries ($expected_count)."
    else
        echo "Table '$table' does not have the expected number of entries. Found $row_count entries, expected $expected_count."
        exit 1
    fi
done

# Clean up temporary dump files
rm "solution.dump"
# clean up local db file
rm "$file1"
