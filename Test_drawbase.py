import turtle as t
import Test_nationalflag


#画旗杆基座
def flagbase():

    #画旗杆基座
    t.penup()
    t.goto(-250,-200)
    t.pendown()#基座起始位置
    t.fillcolor('rosy brown') #设定旗杆基座颜色
    t.begin_fill()
    t.forward(450)
    t.right(75)
    t.forward(100)
    t.right(105)
    t.forward(500)
    t.right(105)
    t.forward(100)
    t.end_fill()

    #在基座框中写校名
    t.penup()
    t.goto(-180,-270)
    t.pendown()
    t.pencolor('gold')
    t.write('浙江传媒学院',font=('楷体',40,'bold'))
    t.penup()

    #画基座的栏杆
    t.penup()
    t.pencolor('black')
    t.goto(-220,-200)
    t.pendown()
    t.fillcolor('gray')
    t.begin_fill()
    t.goto(-220,-150) #画栏杆最左侧第一个竖线
    stepx=30  #X坐标右移步进量
    stepy=25  #Y坐标上下步进量
    c=0 #作为X坐标偏移的倍数计数器
    for i in range(6): #循环六次，画出栏杆相同的部分
        c+=1
        t.goto(-220+c*stepx,-150)
        t.goto(-220+c*stepx,-175)
        c+=1
        t.goto(-220+c*stepx,-175)
        t.goto(-220+c*stepx,-150)

    #补齐栏杆最右侧线条
    c+=1
    t.goto(-220+c*stepx,-150)
    t.goto(-220+c*stepx,-200)
    t.end_fill()


    #画旗杆
    t.penup()
    t.goto(-25,-145)
    t.pensize(10)
    t.setheading(90)
    t.pencolor('steel blue')
    t.pendown()
    t.forward(450)
    
    #画国旗
    t.pensize(1)
    t.setheading(0)
    Test_nationalflag.drawflag(-25,210)
    t.penup()    

if __name__=="__main__":
    flagbase()
