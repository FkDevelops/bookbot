def sort_on(dict):
    return dict["num"]

def number_of_words(text):
    text_words = text.split()
    return len(text_words)

def char_in_text(text):
    lower_case = text.lower()
    char_dict = {}
    for ch in lower_case:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def dict_sort(unsorted):
    dict_list = []
    for ch in unsorted:
        num = unsorted[ch]
        dict_list.append({"char": ch, "num": num})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
    
