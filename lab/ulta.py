first = 0
second = 1
i = 1

print(first)
print(second)
while i <= 100:
    next = first + second
    print(next)
    first = second
    second = next
    i += 1
