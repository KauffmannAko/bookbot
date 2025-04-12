from stats import get_word_count, get_a_character_count

def main(filepath, char_list):
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    char_count = get_a_character_count(book_text, char_list)
    print(word_count)
    print(char_count)

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


main("books/frankenstein.txt",'tpc')
