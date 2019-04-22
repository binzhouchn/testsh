import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())


class Test(object):  # 定义一个类
	def __init__(self，

		func):
	self.__func = func


def __call__(self):  # 定义call方法，当直接调用类的时候，运行这里。
	print('这里是装饰的功能')
	self.__func()


t = Test()  # 实例化对象
t()  # 调用类，将会调用call方法。


@Test  # 类装饰器等于test = Test(test),将函数test当作参数传入类中的init方法，并将函数名赋值给私有属性__func，当函数test被调用的时候，其实是运行Test类中的call方法.
def test():
	print('被装饰的函数')


print(test())
