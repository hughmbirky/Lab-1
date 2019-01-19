import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle Clock")

clock = turtle.Turtle()
clock.color("blue")
clock.pensize(2)
clock.shape("turtle")
clock.stamp()
turn = 30

for t in range(12):
    clock.penup()
    clock.forward(100)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(15)
    clock.stamp()
    clock.home()
    clock.right(turn)
    turn = turn + 30

wn.mainloop()
