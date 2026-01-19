import turtle as t


def motto(startx,starty):
    t.penup()
    t.goto(startx-5,starty)
    t.pendown()
    t.setheading(0)
    t.fillcolor('gold')
    t.begin_fill()
    t.forward(105)
    t.right(90)
    t.forward(350)
    t.right(135)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.right(135)
    t.forward(350)
    t.end_fill()


if __name__=='__main__':
    motto(-200,200)
