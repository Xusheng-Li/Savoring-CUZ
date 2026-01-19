import Test_pentagram
import turtle as t

def drawflag(StartX,StartY):

    #画国旗旗面
    t.speed(10)
   
    t.penup()
    t.setheading(0)
    t.goto(StartX,StartY)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.forward(140)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(140)
    t.left(90)
    t.forward(90)
    t.end_fill()
    t.penup()

    #大五角星，创建1个pentagram类的对象实例并调用画五角星的函数
    big_pentagram=Test_pentagram.pentagram(10,StartX+12,StartY+60,0) 
    big_pentagram.drawstar() 

    #小五角星，创建4个pentagram类的对象实例并调用画五角星的函数
    small_pentagram1=Test_pentagram.pentagram(5,StartX+42,StartY+75,-10)
    small_pentagram1.drawstar()
    small_pentagram2=Test_pentagram.pentagram(5,StartX+42,StartY+37,-10)
    small_pentagram2.drawstar()
    small_pentagram3=Test_pentagram.pentagram(5,StartX+50,StartY+62,10)
    small_pentagram3.drawstar()
    small_pentagram4=Test_pentagram.pentagram(5,StartX+50,StartY+49,0)
    small_pentagram4.drawstar()


if __name__=="__main__":
    drawflag(0,0)
