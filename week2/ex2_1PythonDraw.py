#PythonDraw
import turtle
#库引用
#from turtle import* 直接使用函数名
#import turtle as t 使用t.
turtle.setup(650,350,200,200)
turtle.penup()
#画笔抬起turtle.pu()
turtle.fd(-250)
turtle.pendown()
#画笔落下turtle.pd()
turtle.pensize(5)
#turtle.width()
turtle.pencolor("yellow")
#颜色字符串
#RGB小数值
#RGB元组值
turtle.seth(-40)
for i in range(4):
#range()产生循环计数序列
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
#程序运行之后不会退出
