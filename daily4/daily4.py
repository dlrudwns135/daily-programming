def sub_factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 0

    return (num-1) * (sub_factorial(num-1) + sub_factorial(num-2))

print(sub_factorial(14))