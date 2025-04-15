#!/usr/bin/env python3
from stats import get_word_count, get_a_character_count, report_stats
import sys

def main(filepath, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    char_count = get_a_character_count(book_text, char_list)
    print(word_count)
    report_stats(char_count)

def get_book_text(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

if len(sys.argv) < 3 :
    print("Usage: python3 main.py <path_to_book> <chars>")
    sys.exit(1)
else:
    main(sys.argv[1], sys.argv[2])
