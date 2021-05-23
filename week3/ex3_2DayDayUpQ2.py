#DayDayUpQ2.py
dayfactor=input('请输入：')
dayup=pow(1+eval(dayfactor),365)
daydown=pow(1-eval(dayfactor),365)
print('向上：{:.2f}\t向下：{:.2f}'.format(dayup,daydown))
