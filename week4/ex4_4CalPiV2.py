#CalPiV2.py
from random import random
from time import perf_counter
DARTS=1000*10000
hit=0.0
start=perf_counter()
for i in range(1,DARTS+1):
    x,y=random(),random()
    if (x**2+y**2)**0.5<=1:
        hit=hit+1
pi=4*hit/DARTS
print('圆周率的值为：{:.4f}'.format(pi))
print('程序运行时间：{:.2f}s'.format(perf_counter()-start))
