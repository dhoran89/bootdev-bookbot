def get_num_words(file_txt):
    #split the txt file in to words
    split = file_txt.split()
    count = 0
    for word in split:
        count += 1
        ##print(word)
    return count

def get_char_words(str):
    #gets the number of characters from a string
    dict_count = {}
    string = str.lower()

    for letter in string:
        if letter in dict_count:
            dict_count[letter] += 1
        else:
            dict_count[letter] = 0
            dict_count[letter] += 1
    return dict_count

def sort_on(item):
    return item["num"]

def sort_this(dict):
    list = []
    for key in dict:
        new_dict = {"char": key, "num": dict[key]}
        list.append(new_dict)
    return list
    #print(list)


