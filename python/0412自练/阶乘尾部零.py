def trailingZeros(n):
    num = 0
    while (n):
        num = num + n // 5
        n = n // 5
    return num
print(trailingZeros(185))