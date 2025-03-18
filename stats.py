def count_words(text):
    words = text.split()
    return len(words)

def character_usage(text):
    text_lowercase = text.lower()
    text_set = set(text_lowercase)
    used_chars = {}
    for char in text_set:
        if char.isalpha():
            used_chars[char] = text_lowercase.count(char)
    return used_chars

def dict_to_sorted_list(used_chars):
    sorted_list = sorted(used_chars.items(), key=lambda x: x[1], reverse=True)
    return sorted_list
