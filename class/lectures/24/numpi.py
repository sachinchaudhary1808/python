import pandas as pd
import numpy as np
from numpy import random


x = random.randint(10, size=(3, 2))
y = random.randint(10, size=(2, 4))

print(np.dot(x, y))
