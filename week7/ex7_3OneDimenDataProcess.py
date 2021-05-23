#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex7_3OneDimenDataProcess
#Discription:一维数据处理
f=open('OneD.txt','w',encoding='utf-8')
ls=['英国','委内瑞拉']
f.write('\t'.join(ls))
f.close()

