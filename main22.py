import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())



def function(func): #定义了一个闭包
	def func_in(*args,**kwargs): #闭包内的函数，因为装饰器运行的实则是闭包内的函数，所以这里将需要有形参用来接收原函数的参数。
		print('这里是需要装饰的内容，就是需要添加的内容')
		num = func(*args,**kwargs) #调用实参函数，并传入一致的实参，并且用变量来接收原函数的返回值，
		return num #将接受到的返回值再次返回到新的test()函数中。
	return func_in
@function
def test(a,b): #定义一个函数
	return a+b #返回实参的和

print(test(3,4))