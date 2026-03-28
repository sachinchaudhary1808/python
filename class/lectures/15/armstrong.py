i = 0

while i < 1000:
    sum = 0
    count = 0
    j = i
    while j > 0:
        count += 1
        j //= 10
    j = i
    while j > 0:
        sum += (j % 10) ** count
        j //= 10
    if sum == i:
        print(i)
    i += 1
