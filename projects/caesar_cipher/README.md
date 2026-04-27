# Caesar Cipher

A simple console program that encrypts text using the Caesar cipher.

The program supports both English and Russian alphabets. The user can choose the shift value and the direction of the shift.

## Features

- encrypts text using the Caesar cipher
- supports English letters
- supports Russian letters
- keeps uppercase and lowercase letters
- keeps spaces, punctuation, and other non-letter characters unchanged
- allows shifting characters to the right or to the left
- automatically detects whether the text is English or Russian

## How it works

The Caesar cipher shifts each letter in the text by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text
a → d
b → e
c → f
```

If the shift reaches the end of the alphabet, it starts again from the beginning.

## Run

```bash
python main.py
```

## Usage

After running the program, enter:

1. the text you want to encrypt
2. the shift value
3. the shift direction:
   - `R` for right
   - `L` for left

## Example

```text
Hi! Here you can apply the Caesar cipher to your text
The characters are shifted to the right

Enter the text you want to encrypt: Hello
Enter the offset value: 3
Which way should the cipher be shifted? R - Right, L - Left: r

Khoor
```

## Supported languages

The program supports:

- English alphabet
- Russian alphabet

Mixed English and Russian text is not supported.

## Project structure

```text
caesar_cipher/
├── main.py
└── README.md
```

## Notes

This project was created for Python practice. It helps practice:

- strings
- loops
- functions
- conditions
- working with Unicode characters
- basic encryption logic