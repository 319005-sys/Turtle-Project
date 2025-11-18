import turtle as trtl

def check_win(turtles):
  winning = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
  ]

  positions = []
  for t in turtles:
    if t.isvisible() == True:
      col = t.rect.x // 80
      row = t.rect.y // 80
      index = row * 3 + col
      positions.append(index)

  for a, b, c in winning:
    if a in positions and b in positions and c in positions:
      return True

  return False


turtles = []

for i in range(9):
  turtle = trtl.Turtle()
  turtle.speed(0)
  turtle.penup()
  turtle.shape("circle")
  turtle.turtlesize(3)
  turtle.hideturtle()
  turtles.append(turtle)

drawer = trtl.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()
drawer.goto(-100,-40)
drawer.pendown()
drawer.forward(200)

drawer.penup()
drawer.goto(-100,40)
drawer.pendown()
drawer.forward(200)

drawer.penup()
drawer.goto(-40,-100)
drawer.setheading(90)
drawer.pendown()
drawer.forward(200)

drawer.penup()
drawer.goto(40,-100)
drawer.setheading(90)
drawer.pendown()
drawer.forward(200)

ROWS = 3
COLS = 3
CELL_SIZE = 80
OFFSET_X = -80
OFFSET_Y = -80

positions = []

for i in range(len(turtles)):
    row = i // COLS
    col = i % COLS
    x = OFFSET_X + col * CELL_SIZE
    y = OFFSET_Y + row * CELL_SIZE
    positions.append((x, y))

x=0
for turtle in turtles:
  turtle.goto(positions[x])
  x += 1
  
wn = trtl.Screen()
wn.mainloop()
