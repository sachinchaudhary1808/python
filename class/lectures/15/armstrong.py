i = 0

while i < 1000:
    count = 0
    while i > 0:
        count += (i % 10) * 10
        i /= 10
    print(count)
    i += 1
