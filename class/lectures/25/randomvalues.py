import numpy as np
from numpy import random

li = [
    "tamato",
    "panipuri",
    "uttapam",
    "idli",
    "soya-chunks",
    "roti-daal",
    "chana",
    "coconut-milk",
]

a = random.choice(li)
print(a)
b = np.array(li)
print(b)

random.shuffle(b)
print(b)
