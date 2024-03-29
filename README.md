## Bookbot

### Summary

Bookbot reads a book from a text file,
counts the number of words and characters in the book
and prints the results in a simple book report to the
standard output (console screen).

### Repository mirrors

- **GitHub:** https://github.com/dananglin/bookbot
- **Code Flow:** https://codeflow.dananglin.me.uk/apollo/bookbot

### Requirements

Python version 3.0 or higher.

### Quick guide

Clone this repository.

```sh
git clone https://github.com/dananglin/bookbot.git
cd bookbot
```

You can print the program's help message with the `-h` flag.

```sh
./bookbot -h
```

Download a book in text format (e.g. txt, markdown, etc).
As an example you can download the free ebook called `Frankenstein or The Modern Prometheus` from [here](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt).

```sh
mkdir -p books
curl -L https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt -o books/frankenstein.txt
```

Run Bookbot to produce the book report.

```
$ ./bookbot books/frankenstein.txt
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The character 'a' was found 26743 times
The character 'b' was found 5026 times
The character 'c' was found 9243 times
The character 'd' was found 16863 times
The character 'e' was found 46043 times
The character 'f' was found 8731 times
The character 'g' was found 5974 times
The character 'h' was found 19725 times
The character 'i' was found 24613 times
The character 'j' was found 504 times
The character 'k' was found 1755 times
The character 'l' was found 12739 times
The character 'm' was found 10604 times
The character 'n' was found 24367 times
The character 'o' was found 25225 times
The character 'p' was found 6121 times
The character 'q' was found 324 times
The character 'r' was found 20818 times
The character 's' was found 21155 times
The character 't' was found 30365 times
The character 'u' was found 10407 times
The character 'v' was found 3833 times
The character 'w' was found 7638 times
The character 'x' was found 677 times
The character 'y' was found 7914 times
The character 'z' was found 243 times
--- End report ---
```
