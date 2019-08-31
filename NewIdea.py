import turtle
t=turtle.Turtle()
turtle.setup(800, 800)
def connect_points():
    #t.setpos(789,0)
    x0=(-90,145)
    y0=(190,145)
    mid0=(60,155)


    x1=(-90,0)
    y1=(190,0)
    x2=(-50,-100)
    y2=(140,-100)
    x3=(-45,-115)
    y3=(135,-115)
    mid=(45,-105)
    #leftside line
    turtle.penup()
    turtle.goto(mid0)
    turtle.pendown()
    turtle.goto(x0)
    turtle.pendown()
    turtle.goto(x1)
    turtle.pendown()
    turtle.goto(x2)
    turtle.pendown()
    turtle.goto(x3)
    turtle.pendown()
    turtle.goto(mid)
    turtle.pendown()

    # rightside line
    turtle.penup()
    turtle.goto(mid0)
    turtle.pendown()
    turtle.goto(y0)
    turtle.pendown()
    turtle.goto(y1)
    turtle.pendown()
    turtle.goto(y2)
    turtle.pendown()
    turtle.goto(y3)
    turtle.pendown()
    turtle.goto(mid)
    turtle.pendown()
    turtle.hideturtle()
    turtle.exitonclick()


def set_lip():
    turtle.penup()
    turtle.setpos(0, 25)
    turtle.pendown()
    turtle.circle(100, 45)
    turtle.setheading(0)

connect_points()
set_lip()