#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex6_2
#Discription:BasicStatisticsCal
def getNum():
    nums=[]
    iNumStr=input('请输入需要处理的数据：')
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr=input('请输入需要处理的数据：')
    return nums
def mean(numbers):
    s=0
    for i in numbers:
        s=s+i;
    return s/len(numbers)
def dev(numbers,mean):
    sdev=0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return pow(sdev/len(numbers),0.5)
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=numbers[size//2-1]/2+numbers[size//2]/2
    else:
        med=numbers[size//2]
    return med

n = getNum()
average = mean(n)
dev = dev(n, average)
med = median(n)
print('平均数：{:.2f}方差：{:.2f}中位数：{:.2f}'.format(average, dev, med))




