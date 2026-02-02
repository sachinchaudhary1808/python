# count = 0
# where = input("Go left or right ?: ")

# while where == "right":
#     count += 1
#     if count > 2:
#         print(":(")
#     where = input("Go left or right ?: ")
# print("You got out!")

start = 3
end = 5
ans = 0

for i in range(start, end + 1):
    ans += i

print(ans)
