import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Star")
star = turtle.Turtle()
star.color("gold")
star.pensize(5)

dr = [180, 144, 144, 144, 144]
dx = [100, 100, 100, 100, 100]
for l,r in zip(dr, dx):
    star.left(l)
    star.forward(r)
wn.mainloop()