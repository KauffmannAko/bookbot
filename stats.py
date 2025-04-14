def get_word_count(text):
    list_of_word = text.split()
    return f"Found {len(list_of_word)} total words"

def get_a_character_count(text, chars):
    char_count = {}
    lower_text = text.lower()
    for char in chars:
        char_count[char.lower()] = lower_text.count(char.lower())
 
    return char_count

def report_stats(dic):
    print("--------- Character Count -------")
    lstBook = list(dic.items())
    lstBook.sort(key=lambda x: x[1], reverse=True)
    sorted_dic = dict(lstBook)
    for key, value in sorted_dic.items():
        if not key.isalpha():
            continue
        else:
            print(f"{key}: {value}")
    print("============= END ===============")