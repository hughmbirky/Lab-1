#Question 1
a = "All "
b = "work "
c = "and "
d = "no "
e = "play "
f = "makes "
g = "Jack "
h = "a "
i = "dull "
j = "boy"
print(a+b+c+d+e+f+g+h+i+j)

#Question 2
print(6*(1-2))

#Question 3
print("hi")
#comment print("hi")
#Nothing happens because it sees the code as a comment

#Question 4
#See picture

#Question 5
P = 10000
r = 0.08
n = 12
response = input("Compounded years: ")
t = float(response)
Area = (P*(1+(r/n))**(n*t))
print("The amount of money saved is $",Area)

#Question 6
#Guesses: a=1, b=4, c=3, d=12, e=0, f= 0, 7=error
print(5%2)
print(9%5)
print(15%12)
print(12%15)
print(6%6)
print(0%7)
print(7%0)
#It is impossible to divide by zero, hence, there is an error

#Question 7
#Your alarm goes off two days later at 5:00pm

#Question 8
response = input("What time is it in military time? (Hours): ")
ti = int(response)
responses = input("How long must we wait?: ")
h = int(responses)
print("In military time, the alarm will go off at",h % 12 + ti, "hours")
