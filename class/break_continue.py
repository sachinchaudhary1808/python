# Lecture 14
# break and continue

a = int(input())
i = 0

for i in range(0, a):
    if i % 2 == 0:
        continue
    print(i)

# while True:
#     if i == a:
#         break
#     print(i)
#     i = i + 1
