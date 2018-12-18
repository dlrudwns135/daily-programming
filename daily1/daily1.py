def GetHex(dec):
    return format(dec, '#04x')[2:]


def Hexcolor(dec1, dec2, dec3):
    return '#' + GetHex(dec1) + GetHex(dec2) + GetHex(dec3)
    #return '#' + To_hex(dec1) + To_hex(dec2) + To_hex(dec3) #another answer


def To_hex(dec):
    return To_hexvalue(int(dec/16)) + To_hexvalue(dec%16)


def To_hexvalue(dec):
    if dec/10:
        return chr(ord('A') + (dec%10))
    else:
        return chr(ord('0') + (dec%10))


def blend(obj):
    value = {'r':0,'g':0,'b':0};
    for i in obj:
        value.__setitem__('r',int(value.get('r')) + int(i[1:3],16))
        value.__setitem__('g', int(value.get('g')) + int(i[3:5],16))
        value.__setitem__('b', int(value.get('b')) + int(i[5:7],16))
    value.__setitem__('r', round(value.get('r')/obj.__len__()))
    value.__setitem__('g', round(value.get('g') / obj.__len__()))
    value.__setitem__('b', round(value.get('b') / obj.__len__()))
    return Hexcolor(value.get('r'), value.get('g'), value.get('b'))