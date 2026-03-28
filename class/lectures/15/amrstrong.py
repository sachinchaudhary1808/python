i = 0
while i < 1000:
    count = 0
    temp = i
    result = 0
    while temp > 0:
        temp //= 10
        count += 1
    temp = i
    while temp > 0:
        result += (temp % 10) ** count
        temp //= 10
    if result == i:
        print(i)
    i += 1
