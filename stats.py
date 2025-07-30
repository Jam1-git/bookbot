def word_count(text_as_string):
    words = text_as_string.split()
    return len(words)

def char_count(text_as_string):
    characters = {}
    for char in text_as_string:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    
    return characters

def sorted_characters(characters_dict):
    dictionary_list = []
    for i in characters_dict:
        if i.isalpha():
            dictionary_list.append({"character": i, "num": characters_dict[i]})
        else:
            continue
    def sort_on(item):
        return item["num"]
    
    dictionary_list.sort(reverse = True, key = sort_on)

    return dictionary_list



