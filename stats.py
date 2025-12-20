#stats.py


#Accepts text of book as string and returns word count
def get_num_words(book_text):
    return len(book_text.split())

def get_num_char(book_text):
    char_counts = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in char_counts:
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_num_char(count_dict):
    list_of_char = []
    for char in count_dict:
        char_dict = {"char": char, "num": count_dict[char]}
        list_of_char.append(char_dict)
    list_of_char.sort(reverse=True, key=sort_on)
    return list_of_char


