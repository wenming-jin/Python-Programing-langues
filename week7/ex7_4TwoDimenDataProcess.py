#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex7_4TwoDimenDataProcess
#Discription:
fname='TwoD.csv'
fo=open(fname)
ls=[]
for line in fo:
    line=line.replace('\n','')
    ls.append(line.split(','))
fo.close()
print(ls)