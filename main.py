import turtle as trtl
import random 

ROWS = 3
COLS = 3
CELL_SIZE = 80
OFFSET_X = -80
OFFSET_Y = -80

def check_win(board):
    winning = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8), 
        (0,4,8),
        (2,4,6)         
    ]
    for a,b,c in winning:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    return None


drawer = trtl.Turtle()
drawer.hideturtle()
drawer.speed(0)

def draw_board():
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

draw_board()

turtles = []
board = [""] * 9 

for i in range(9):
    t = trtl.Turtle()
    t.speed(0)
    t.penup()
    t.shape("circle")
    t.fillcolor("white")
    t.turtlesize(3)
    turtles.append(t)

positions = []
for i in range(9):
    row = i // COLS
    col = i % COLS
    x = OFFSET_X + col * CELL_SIZE
    y = OFFSET_Y + row * CELL_SIZE
    positions.append((x, y))

for i, t in enumerate(turtles):
    t.goto(positions[i])

turn = "X"
game_over = False
wn = trtl.Screen()
color = True

def handle_click(x, y, index):
    global turn, game_over, color
    
    if game_over:
        return
    if board[index] != "":
        return

    t = turtles[index]
    if color == True:
      t.color("blue")
      color = False
    else:
      t.color("purple")
      color = True
    
    t.turtlesize(0.01)
    t.write(turn, font=("Arial", 30, "bold"), align="center")
    board[index] = turn

    winner = check_win(board)
    if winner:
        show_winner(winner)
        game_over = True
        return
    if "" not in board:
        tie_game()
        game_over = True
        return
    turn = "O" if turn == "X" else "X"

def show_winner(winner):
    msg = trtl.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 120)
    msg.color("green")
    msg.write(f"{winner} wins!", align="center", font=("Arial", 32, "bold"))
    
def tie_game():
    msg = trtl.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 120)
    msg.color("red")
    msg.write(f"Tie Game!", align="center", font=("Arial", 32, "bold"))
    

    

for i, t in enumerate(turtles):
    t.onclick(lambda x, y, i=i: handle_click(x, y, i))

wn.mainloop()
