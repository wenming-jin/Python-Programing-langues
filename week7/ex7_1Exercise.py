#Author:WenmingJin
#CreateTime:2021/5/23
#FileName:ex7_1Exercise
#Discription:练习
# tf=open('text.txt','rt',encoding = "utf-8")
# bf=open('text.txt','rb')
# print(tf.readlines())
# print(bf.readline())
# f=open('f.txt','w')
# tf.close()
# bf.close()
# f.close()
# fname=input('请输入要打开文件信息：')
# fo=open(fname,'r')
# txt=fo.read()
#
# fo.close()
fo=open('output.txt','w+')
ls=['中国','法国','美国']
fo.writelines(ls)
fo.seek(0)#指针返回到文件最开始
for line in fo:
    print(line)
fo.close()
