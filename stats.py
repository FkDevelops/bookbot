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
