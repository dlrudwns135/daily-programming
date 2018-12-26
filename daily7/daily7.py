def crypt_caesar(input):
    string = input.split(' ')[1].lower()
    move = ord(input.split(' ')[0].lower()[0])-97
    return ''.join([chr(ord(i)+move if ord(i)+move < 123 else ord(i)+move-26) for i in string])


# print(crypt_caesar('snitch thepackagehasbeendelivered'))
