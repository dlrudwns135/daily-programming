def getHex(dec):
    return format(dec, '#04x')[2:]


def hexcolor(dec1, dec2, dec3):
    return '#' + getHex(dec1) + getHex(dec2) + getHex(dec3)
