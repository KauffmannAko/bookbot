from stats import get_word_count

def main(filepath):
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    print(word_count)

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


main("books/frankenstein.txt")