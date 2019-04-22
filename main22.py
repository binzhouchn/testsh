import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())

def num():
	a,b = 0,1
	for i in range(10):
		yield b  #生成关键字yield，有yield的关键字的代码块就是yield的生成器。当运行到yield时代码就会停止，并返回运行结果，当在次运行时依旧是到yield停止，并返回结果。 切记：生成器只能使用next方法。
		a,b = b,a+b
		temp = yield b  #这里并不是变量的定义，当运行到yield时就会停止，所以当运行到等号右边的时候就会停止运行，当在次使用next的时候，将会把一个None赋值给temp，因为b的值已经在上轮循环中输出。这里可以使用num().send()方法将一个新的值赋值给temp。
a = num()
print(a)
