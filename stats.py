def number_of_words(get_book_text):
    num_words_split = get_book_text.split()
    num_words = len(num_words_split)
    return num_words
def number_of_char(get_book_text):
    text_lower = get_book_text.lower()
    char_count = {}
    for character in text_lower:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count
def sort_on(number):
    return number["num"]
def sorted_format(char_count):
    char_list=[]
    for new_char in char_count:
        some_char = char_count[new_char]
        structure_dic = {"char": new_char, "num": some_char}
        char_list.append(structure_dic)
        char_list.sort(reverse=True, key=sort_on)
    return char_list