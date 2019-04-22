import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())


def function(func):  # 定义了一个闭包
    def func_in(*args, **kwargs):  # 闭包内的函数，因为装饰器运行的实则是闭包内的函数，所以这里将需要有形参用来接收原函数的参数。
        print('这里是需要装饰的内容，就是需要添加的内容')
        func(*args, **kwargs)  # 调用实参函数，并传入一致的实参。

    return func_in


@function  # 装饰器的python写法，等价于test = function(test) .
def test():
    print('无参函数的测试')


test(5，6)
