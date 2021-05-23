#CalPiV1.py
pi=0
N=10000
for k in range(N):
    pi=pi+1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print('圆周率的值为：{:.20f}'.format(pi))
