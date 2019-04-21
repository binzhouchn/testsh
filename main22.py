import numpy as np
import pandas as pd
import sklearn
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())

class A:
    @staticmethod
    def ff(x):
        return x * 3

print('--------------------')

print(A.ff(10))