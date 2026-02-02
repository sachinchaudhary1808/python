n = int(input("enter the number: "))
count = len(str(n))
total = 0

for char in str(n):
    total += int(char) ** count

if total == n:
    print("number is armstrong")
else:
    print("number is not armstrong")

i = 0
while i <= 1000:
    total = 0
    count = len(str(i))

    for char in str(i):
        total += int(char) ** count
    if total == i:
        print(i)
    i += 1
