import turtle

wn = turtle.Screen()
wn.title('Pingpong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgpic('blue.png')


#Score
sa = 0
sb = 0
#Paddle A
pa = turtle.Turtle()
pa.speed(0)
pa.shape('square')
pa.shapesize(stretch_wid=7,stretch_len=1)
pa.color('red')
pa.penup()
pa.goto(-350,0)

#Paddle B
pb = turtle.Turtle()
pb.speed(0)
pb.shape('square')
pb.shapesize(stretch_wid=7,stretch_len=1)
pb.color('red')
pb.penup()
pb.goto(350,0)

#Ball
b = turtle.Turtle()
b.speed(0)
b.shape('circle')
b.color('white')
b.penup()
b.goto(0,0)
b.dx = 0.5
b.dy = 0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Scoreboard', align='center',font=('Courier',24,'normal'))
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write('Syah : 0  Hanu : 0', align='center',font=('Courier',24,'normal'))


#Function
def pa_up():
    y=pa.ycor()
    y+= 20
    pa.sety(y)

def pa_down():
    y=pa.ycor()
    y-= 20
    pa.sety(y)

def pb_up():
    y=pb.ycor()
    y+= 20
    pb.sety(y)

def pb_down():
    y=pb.ycor()
    y-= 20
    pb.sety(y)

#Keyboardbinding
wn.listen()
wn.onkeypress(pa_up,'w')
wn.onkeypress(pa_down,'s')
wn.onkeypress(pb_up,'Up')
wn.onkeypress(pb_down,'Down')


#Maingameloop
while True:
    wn.update()

    #Movetheball
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

    #borderchecking
    if b.ycor()>290:
        b.sety(290)
        b.dy *=-1

    if b.ycor()<-290:
        b.sety(-290)
        b.dy *=-1

    if b.xcor()>390:
        b.goto(0,0)
        b.dx *=-1
        sa += 1
        pen.clear()
        pen.write(f'Syah : {sa}  Hanu : {sb}', align='center',font=('Courier',24,'normal'))

    if b.xcor()<-390:
        b.goto(0,0)
        b.dx *=-1
        sb += 1
        pen.clear()
        pen.write(f'Syah : {sa}  Hanu : {sb}', align='center',font=('Courier',24,'normal'))
    #paddleslapball
    if (b.xcor()>340 and b.xcor()<350) and (b.ycor()<pb.ycor()+65 and b.ycor()>pb.ycor()-65):
        b.setx(340)
        b.dx *=-1

    if (b.xcor()<-340 and b.xcor()>-350) and (b.ycor()<pa.ycor()+65 and b.ycor()>pa.ycor()-65):
        b.setx(-340)
        b.dx *=-1
