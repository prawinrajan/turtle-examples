import turtle

t=turtle.Turtle()

t.penup()
t.setx(10)
t.sety(10)
t.dot(10,"red")

t.setx(40)
t.sety(10)
t.dot(10,"blue")

t.setx(10)
t.sety(40)
t.dot(10,"green")
t.pendown()
t.hideturtle()
#t.exitonclick()
t.speed(40000)
#t.done()