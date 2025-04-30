def get_num_words(text):
    return len(text.split())

from collections import defaultdict

def get_num_chars(text):
    result = defaultdict(int)
    for char in text:
        char = char.lower()
        result[char] += 1
    return result

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    chars = []
    for key in dict:
        chars.append({"char": key, "num": dict[key]})
    chars.sort(reverse=True, key=sort_on) 
    return chars
