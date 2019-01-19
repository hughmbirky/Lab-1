#Question 3
for j in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("One of the months of the year is " + j)
#Question 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#a
for l in xs:
    print(l)
#b
for l in xs:
    print(l, l**2)
#c
total = 0
for l in xs:
    total = total + l
print(total)
#d
total = 1
for l in xs:
    total = total*l
print(total)

#Question 6
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Shapes")

hugh = turtle.Turtle()
hugh.color("pink")
hugh.pensize(5)

#triangle
for l in [120, 120, 120]:
    hugh.forward(l)
    hugh.left(l)

joe = turtle.Turtle()
joe.color("purple")
joe.pensize(5)
#square
for l in [90, 90, 90, 90]:
    joe.forward(l)
    joe.left(l)

bill = turtle.Turtle()
bill.color("red")
bill.pensize(5)
#hexagon
for l in [60, 60, 60, 60, 60, 60]:
    bill.forward(l)
    bill.left(l)

rex = turtle.Turtle()
rex.color("blue")
rex.pensize(5)
#octagon
for l in [45, 45, 45, 45, 45, 45, 45, 45]:
    rex.forward(l)
    rex.left(l)

wn.mainloop()

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
#Question 8
#see below and questoin 7
print(drunk.position())
#Question 9
#You would need to turn 20 degrees each time
#Question 10
#I guess that this will not do anything immediately
#Nothing happened

#This will open a screen that is white
#It opened a white screen

#This will create a small pointer in the middle of the screen
#It created a small black pointer in the middle of the screen

#this will cause the pointer to turn 90 degrees to the right
#It caused the pointer to turn 90 degrees to the right

#this will cause the pointer to turn in a circle to the left 10 times
#It caused the pointer to turn in a circle to the left 10 times

#this will cause the pointer to turn to the left 90 degrees
#It caused the pointer to turn to the left 90 degrees

#this will cause the pointer to do the next function very quickly
#It did nothing

#this will cause the pointer to turn in a circle to the left 10 times
#It turned in a circle to the left 10 times much faster

#this will cause the pointer to this will cause the next motion to not move or at least move very slowly
#It did nothing

#this will cause the pointer to turn in a cirlce to the left 10 times and the to the left 45 degrees
#It immediately turned to 45 degrees to the left

#this will cause the pointer to move backwards 100 units
#It moved backwards 100 units
#I scored 10/11 points

#Question 11
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
#Question 12
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






