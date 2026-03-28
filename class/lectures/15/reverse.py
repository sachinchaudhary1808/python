i = 0

while i < 1000:
    j = i
    rev = 0
    while j > 0:
        rev = (rev * 10) + (j % 10)
        j //= 10

    print(rev)
    i += 1
