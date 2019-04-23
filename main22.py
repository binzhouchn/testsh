import numpy as np
import pandas as pd
import sklearn
import copy
from tqdm import tqdm, tqdm_notebook
import os
print(os.getcwd())


def work():
	global num
	l.acquire()  # 这里表示调用互斥锁上锁方法，如果work函数先运行l.acquire的话，那么后边的程序就不能再修改和使用变量num。直到将其解锁后才能使用。
	for i in range(1000000):
		num += 1
	print('work的num是%d' % num)
	l.release()  # 这里表示调用互斥锁解锁方法。