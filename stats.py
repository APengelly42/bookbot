def create_sorted_dict(dict):
    data = [(k, v) for k, v in dict.items()]
    data.sort(key = lambda k: k[1], reverse = True)
    result = []
    for item in data:
        result.append({"char": item[0], "num": item[1]})

    return result

def get_char_count(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 0
        char_dict[char.lower()] += 1

    return char_dict

def get_word_count(text):
    text = text.replace('\n', ' ')
    words = len([x for x in text.split(' ') if x])
    return words
