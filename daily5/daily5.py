data = [data.strip() for data in open('enable1_word_list', 'r')]

def count_find_string(string):
    strings = []
    for i in range(0, string.__len__()):
        substring = string[:i] + string[i+1:]
        if substring in data:
            strings.append(substring)