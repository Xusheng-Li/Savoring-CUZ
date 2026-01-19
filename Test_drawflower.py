import turtle as t

 
#定义画叶子和花瓣叶片的函数
def draw_leaf():
    t.speed(10)
    for i in range(0,2):
        for j in range(0,15):
            t.forward(2)
            t.left(6)
        t.left(90)

#定义画绿叶和花朵的函数  
def drawflower(StartX,StartY,Color):
    t.speed(10)
    t.penup()
    t.goto(StartX,StartY)
    t.pendown()
    t.pencolor('black')
    
    #画杆和叶子
    t.left(90)
    t.down()
    t.forward(10)
    t.fillcolor("green")
    t.begin_fill()
    draw_leaf()
    t.end_fill()

    t.forward(10)
    t.left(270) #准备画右面叶子
    t.fillcolor("green")
    t.begin_fill()
    draw_leaf()
    t.end_fill()

    t.left(90)
    t.forward(30)
    t.fillcolor(Color)
    t.begin_fill()

    #画花瓣
    for i in range(6):
        draw_leaf()  #6六次调用花瓣函数，每次向左偏离60度，整好6*60完成一圈
        t.left(60)
    t.end_fill()

    
if __name__=="__main__":
    drawflower(0,0,'red')

    
