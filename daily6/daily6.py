numbers = [([' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']),
           ([' ', ' ', ' '], [' ', ' ', '|'], [' ', ' ', '|']),
           ([' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']),
           ([' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']),
           ([' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']),
           ([' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']),
           ([' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']),
           ([' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']),
           ([' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']),
           ([' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|'])
           ]


def parse_string(input_string):
    str_to_list = [list(string) for string in input_string.split('\n')]
    return str_to_list


def check_number(str_to_list):
    num_list = []
    for i in range(0, int(str_to_list[0].__len__() / 3)):
        num = ([str_to_list[0][i*3],str_to_list[0][i*3+1],str_to_list[0][i*3+2]],
               [str_to_list[1][i*3],str_to_list[1][i*3+1],str_to_list[1][i*3+2]],
               [str_to_list[2][i*3],str_to_list[2][i*3+1],str_to_list[2][i*3+2]])
        num_list.append(num)
    return ''.join([str(numbers.index(d)) for d in num_list])


# data = parse_string('''    _  _     _  _  _  _  _
#   | _| _||_||_ |_   ||_||_|
#   ||_  _|  | _||_|  ||_| _|''')
#
# print(check_number(data))