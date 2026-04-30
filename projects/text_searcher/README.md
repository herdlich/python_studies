# Text Searcher

A simple console program that searches for a word in several text files.

## Features

- searches for a word in `.txt` files
- search is case-insensitive
- shows the file name where the word was found
- shows the line number
- highlights the searched word with angle brackets
- prints a message if nothing is found
- saves search results to `result.txt`

## Project structure

```text
text_searcher/
├── main.py
├── README.md
├── result.txt
└── texts/
    ├── note1.txt
    ├── note2.txt
    └── note3.txt
```

## How it works

The program searches through the files inside the `texts/` folder.

If the searched word is found, the program prints the result to the console and saves it to `result.txt`.

Example output:

```text
file: note1.txt, line: 2: this line contains <PYTHON>
```

## Run

```bash
python main.py
```

## Example

```text
Enter your word for search: python
file: note1.txt, line: 1: <PYTHON> is a popular programming language.
file: note2.txt, line: 2: i use <PYTHON> for automation.
```

The same result will be saved to:

```text
result.txt
```

## Notes

The current version has one main drawback: the entire matched line is converted to lowercase before highlighting the searched word.

For example:

```text
Python is a Popular Programming Language.
```

becomes:

```text
<PYTHON> is a popular programming language.
```

This project was created for practicing:

- working with files
- reading text files
- writing results to a file
- loops
- functions
- string methods
- case-insensitive search
- `enumerate()`