def upc_check(inp):
    data = str(inp).zfill(11)
    cal = 0
    for i in range(1, 12):
        if i % 2 == 1:
            cal += int(data[i - 1])
    cal *= 3
    for i in range(1, 12):
        if i % 2 == 0:
            cal += int(data[i - 1])
    result = cal % 10

    return 0 if result == 0 else 10 - result


print(upc_check(1234567))
