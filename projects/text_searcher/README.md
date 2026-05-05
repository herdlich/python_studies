# Text Search Tool

Simple Python script to search for a word across multiple `.txt` files in a folder.

## Features

- Searches all `.txt` files in a directory
- Case-insensitive matching
- Shows line numbers for each match
- Outputs results to both console and file (`results.txt`)
- Displays match count per file and total matches

## How it works

1. Place your `.txt` files inside the `texts/` folder
2. Run the script
3. Enter a search term
4. View results in:
   - Console output
   - `results.txt` file

## Example output

file1.txt:
1 line: example text
3 line: another match
Matches: 2

Total number of matches: 2

## Requirements

- Python 3.x

## Notes

- The results file is overwritten on each run
- Only `.txt` files are processed