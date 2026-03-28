i = 2
j = 1

while i < 6:
    j = 1
    while j < i:
        print("*", end="")  # space
        j += 1
    print("")  # new line
    i += 1
