def GetHex(dec):
    return format(dec, '#04x')[2:]


def Hexcolor(dec1, dec2, dec3):
    #return '#' + GetHex(dec1) + GetHex(dec2) + GetHex(dec3)
    return '#' + To_hex(dec1) + To_hex(dec2) + To_hex(dec3) #another answer


def To_hex(dec):
    return To_hexvalue(int(dec/16)) + To_hexvalue(dec%16)


def To_hexvalue(dec):
    if dec/10:
        return chr(ord('A') + (dec%10))
    else:
        return chr(ord('0') + (dec%10))