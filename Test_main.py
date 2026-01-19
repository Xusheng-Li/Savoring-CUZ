import Test_drawbase  #调用画旗杆基座的外部函数（模块）
import Test_drawflower  #调用画花朵的外部函数（模块）
import Test_schoolmotto  #调用画校训的外部函数（模块）
import turtle as t  #用字母t来代替turtle。

def main():

    t.speed(10) #设定画笔速度

    #设置画布背景
    t.bgcolor('cornflower blue')
    
    
    #校训
    t.pencolor('red')
    Test_schoolmotto.motto(-360,200)
    t.penup()
    t.goto(-335,-50)
    t.pendown()
    t.write('敬\n业\n\n博\n学',font=('楷体',32,'bold'))

    Test_schoolmotto.motto(220,200)
    t.penup()
    t.goto(245,-50)
    t.pendown()
    t.write('求\n真\n\n创\n新',font=('楷体',32,'bold'))

    t.penup()
    t.setheading(0)
    t.pencolor('black')
    
    #画基座、旗杆和国旗
    Test_drawbase.flagbase()


    #画基座前的花坛
    X=-320  #设置第一朵花的初始位置X坐标
    Y=-350  #设置第一朵花的初始位置X坐标

    t.penup()   
    t.goto(X,Y)
    for i in range(0,7): #画7朵花，交叉红花和黄花
        t.pendown()
        t.setheading(0)
        if i%2==0:
            Test_drawflower.drawflower(X,Y,'red')
        else:
            Test_drawflower.drawflower(X,Y,'yellow')
        X=X+100  #依次向右移动100个点的位置
        t.penup()


if __name__=="__main__":
    main()
