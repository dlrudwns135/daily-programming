def compare_string(string1, string2):
    testdata = []
    for i in range(1, string1.__len__() + 1):
        testdata.append(string1[:i - 1] + string1[i:])

    if string2 in testdata:
        return True
    else:
        return False


def bonus1(word):
    enable_strings = [data.strip() for data in open('enable1_word_list', 'r')]
    find_strings = []
    for i in range(0, len(word)):
        find_string = word[:i] + word[i+1:]
        if find_string in enable_strings and find_string not in find_strings:
            find_strings.append(find_string)
    return find_strings
