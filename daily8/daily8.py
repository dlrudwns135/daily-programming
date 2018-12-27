import random


def roll_dice(dice):
    split_string = dice.split('d')
    sum = 0
    for i in range(0,int(split_string[0])):
        sum += random.randint(2,int(split_string[1]))
    return sum


# print(roll_dice('4d12'))