import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())


def function(func):  # 定义了一个闭包
    def func_in():  # 闭包内的函数
        print('这里是需要装饰的内容，就是需要添加的内容')
        func()  # 调用实参函数。

    return func_in


def test():  # 需要被装饰修改的函数。
    return '无参函数的测试'

a = function(test())
print(a)