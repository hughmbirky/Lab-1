#pt: 1

def gcf(x,y):
  if y > x: #check for which one to take the module of
      if y % x == 0: #what should happen when there is no remainder between the two numbers
          print(x)
      else: #if there is a remainder
          return gcf(y % x, x) #run again but start with the remainder and x
  else: #if x > y
      if x % y == 0:
          print(y)
      else:
          return gcf(y, x % y)
gcf(49,7)


#pt: 2

def checkeven(x):
    if x % 2 == 0: #check if divisible by two
        print("True")
    else:
        print("False")
checkeven(7890345790843798798)


# pt: 3

def authenticate():
    response = input("USERNAME: ")
    t = str(response)
    if t == "User Name":
        answer = input("PASSWORD: ")
        s = str(answer)
        if s == "Pass Word":
            print("Login Successful")
        else:
            print("Login Failed")
    else:
        print("Login Failed")

authenticate()

