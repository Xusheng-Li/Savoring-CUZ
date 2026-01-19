import turtle as t

#定义五角星类
class pentagram:

    #初始函数，兼给类的初始变量赋值
    def __init__(self,LENGTH,X,Y,ANG): 
        self.__linelength=LENGTH
        self.__startx=X
        self.__starty=Y
        self.__startang=ANG
        
    #画五角星的函数
    #def drawstar(self,LENGTH,X,Y,ANG):
    def drawstar(self):
        t.speed(10)
        t.goto(self.__startx,self.__starty)
        t.setheading(self.__startang)
        t.pendown()
        t.fillcolor('yellow')
        t.begin_fill()
        for i in range(1,6):
            t.forward(self.__linelength)
            t.left(72)
            t.forward(self.__linelength)
            t.right(144)
        t.end_fill()
        t.penup()
        t.hideturtle()
    
