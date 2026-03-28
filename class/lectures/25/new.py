import numpy as np

print(np.sin([60]))
print(np.cos([60]))

x = [6, 1, 0, 4, 7]
y = [67, 57, 77, 81, 72]
print("sigma x =", np.sum(x))
print("sigma y =", np.sum(y))

print(np.dot(x, y))
print(np.sum(np.dot(x, y)))

print("sigma of x =", np.dot(x, y))

sumx2 = np.sum(np.dot(x, x))
sumx = np.sum(x)
sumy = np.sum(y)
sumxy = np.sum(np.dot(x, y))
n = len(x)
b = ((n * sumxy) - (sumx * sumy)) / ((n * sumx2) - (sumx * sumx))
print(b)

print("-------------------------------------")
print("-------------------------------------")

print("------------np.square-------------")
print(np.square(x))

print("------------np.std-------------")
print(np.std(x))
print("------------np.mean-------------")
print(np.mean(x))
# variations
print("------------np.var-------------")
print(np.var(x))


# square root ke liye sqrt  and for square use np.square
