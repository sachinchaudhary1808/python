list = []
while True:
    a = input("Enter number, say 'no' if u wanna stop.")
    if a == "no":
        break
    list.append(int(a))

print(list)

list1 = []
while True:
    a = input("Enter number, say 'no' if u wanna stop.")
    if a == "no":
        break
    list1.append(int(a))

print(list1)
# extend returns nothing
list2 = list.extend(list1)
print(list2)
print(list)

list.insert(3, 52)
print(list)
list.remove(52)
print(list)

i = list.count(1)
print(i)

# last wala footega
i = list.pop(1)
print(i)
print(list)

i = list.pop(1)
print(i)
print(list)

# line mai laga denge
list.sort()
print(list)

# chote wale pahle
list.reverse()
print(list)

# mardo sabko
list = []
