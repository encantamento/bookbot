def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_num_char(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_char_list(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

