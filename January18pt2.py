#functions
import turtle
t = turtle

def draw_square(t, sz): #make turtle t draw a square size sz
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a funciton")
t.speed(3)

draw_square(t, 150) #call the funciton to draw the square

wn.mainloop()
