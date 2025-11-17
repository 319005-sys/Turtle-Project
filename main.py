#this is where we will save our code
import turtle as trtl

turtles = []

'''
turtle1 = trtl.Turtle()
turtle2 = trtl.Turtle()
turtle3 = trtl.Turtle()
turtle4 = trtl.Turtle()
turtle5 = trtl.Turtle()
turtle6 = trtl.Turtle()
turtle7 = trtl.Turtle()
turtle8 = trtl.Turtle()
turtle9 = trtl.Turtle()
turtles.append(turtle1)
turtles.append(turtle2)
turtles.append(turtle3)
turtles.append(turtle4)
turtles.append(turtle5)
turtles.append(turtle6)
turtles.append(turtle7)
turtles.append(turtle8)
turtles.append(turtle9)
'''

for i in range(9):
  turtle = trtl.Turtle()
  turtle.hideturtle()
  turtles.append(turtle)

drawer = trtl.Turtle()
  
wn = trtl.Screen()
wn.mainloop()
