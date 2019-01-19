#Question 7
import turtle
wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Drunk")
drunk = turtle.Turtle()
drunk.color("black")
drunk.pensize(5)

dr = [160, -43, 270, -97, -43, 200, -940, 17, -86]
dx = [100, 100, 100, 100, 100, 100, 100, 100, 100]
for l,r in zip(dr, dx):
    drunk.left(l)
    drunk.forward(r)
    print(drunk.position())

wn.mainloop()

