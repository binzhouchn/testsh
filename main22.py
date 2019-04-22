import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())

a = 9
b = a
print(id(a) == id(b))

print('second scenario')

a = [1,2,3]
b = copy.deepcopy(a)
print(id(a) == id(b))

print('--------------------')

print(list(range(0, 10, 2)))