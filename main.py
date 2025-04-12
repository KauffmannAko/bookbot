
def main(filepath):
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    print(word_count)

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def get_word_count(text):
    list_of_word = text.split()
    return f"{len(list_of_word)} words found in the document"




main("books/frankenstein.txt")