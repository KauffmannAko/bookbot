def get_word_count(text):
    list_of_word = text.split()
    return f"{len(list_of_word)} words found in the document"

def get_a_character_count(text, chars):
    char_count = {}
    lower_text = text.lower()
    for char in chars:
        char_count[char.lower()] = lower_text.count(char.lower())
 
    return char_count