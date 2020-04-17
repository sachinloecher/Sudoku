import turtle, random

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x=-150
topLeft_y=150
intDim = 35
active_col = -1
active_row = -1

'Solver'
# Find empty cell
def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                return(i, j)
    return None
# Check if board valid
def check_valid(boa, num, pos):
    #check row
    for j in range(len(boa[0])):
        if boa[pos[0]][j] == num and pos[1] != j:
            return False
    #check column
    for i in range(len(boa)):
        if boa[i][pos[1]] == num and pos[0] != i:
            return False
    #check box
    boxI = pos[0] -(pos[0] % 3)
    boxJ = pos[1] -(pos[1] % 3)
    for i in range(int(len(boa)/3)):
        for j in range(int(len(boa[0])/3)):
            if boa[boxI + i][boxJ + j] == num and pos[0] != (boxI + i) and pos[1] != (boxJ + j):
                return False
    return True
# Recursive solver
def findsolution(boa):
    global grid
    pos = find_empty(boa)
    if not pos:
        return True
    else:
        row, col = pos
    
    for n in range(1, len(boa) + 1):
        if check_valid(boa, n, pos):
            boa[row][col] = n
        
            if findsolution(boa):
                grid = boa
                return True
            
            
            boa[row][col] = 0
    
    return False


'GUI'
# Display Solution
def h1():
    findsolution(grid)
    myPen.clear()
    drawGrid()
    drawnum(grid)
    text("Sudoku Grid Solved",-110,-210,20)
# Dipplay Numbers
def drawnum(grid):
    for row in range (0,9):
        for col in range (0,9):
            if grid[row][col]!=0:
                text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)
# Display Grid
def drawGrid():
    global myPen
    global intDim
    myPen.color("#000000")
    
    for row in range(0,10):
      if (row%3)==0:
        myPen.pensize(4)
      else:
        myPen.pensize(2)
      myPen.penup()
      myPen.goto(topLeft_x,topLeft_y-row*intDim)
      myPen.pendown()
      myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    for col in range(0,10):
      if (col%3)==0:
        myPen.pensize(4)
      else:
        myPen.pensize(2)    
      myPen.penup()
      myPen.goto(topLeft_x+col*intDim,topLeft_y)
      myPen.pendown()
      myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)
# Display Text
def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.color("#000000")
    myPen.penup()
    myPen.goto(x,y)    		  
    myPen.write(message,align="left",font=FONT)


'Generator'
# Rotate List Left 3 & 4
def shift_grid(grid):
    global row
    for i in range(1, 9):
        if i%3 == 0:
            row = row[4:] + row[:4]
            grid.append(row)
        else:
            row = row[3:] + row[:3]
            grid.append(row)
    return grid
# Switch Rows Randomly
def switch_rows(grid):
    for b in range(0, 3):
        switch = random.sample(range(0, 3), 2)
        temp = grid[switch[0] + b*3]
        grid[switch[0] + b*3] = grid[switch[1] + b*3]
        grid[switch[1] + b*3] = temp
    return grid
# Switch Columns Randomly
def switch_2_columns(grid, switch, b):
    n = len(grid)
    for i in range(0, n):
        temp = grid[i][switch[0] + b*3]
        grid[i][switch[0] + b*3] = grid[i][switch[1] + b*3]
        grid[i][switch[1] + b*3] = temp
    return grid
def switch_columns(grid):
    for b in range(0, 3):
        switch = random.sample(range(0, 3), 2)
        grid = switch_2_columns(grid, switch, b)
    return grid
# Remove 35 Numbers
def remove_numbers(grid):
    for i in range(0, 36):
        grid[random.randrange(len(grid[0]))][random.randrange(len(grid))] = 0
    return grid
# Generate Random Sudoku Board
def generate_sudoku():
    matrix = []
    global row
    row = ((random.sample(range(1, 10), 9)))
    matrix.append(row)
    shift_grid(matrix)
    switch_rows(matrix)
    switch_columns(matrix)
    remove_numbers(matrix)
    return matrix

grid = generate_sudoku()
grid0 = grid.copy()

def activate_box(x, y):
    global grid0
    global grid
    global active_col, active_row
    if active_col != -1 and active_row != -1:
        deactivate_box(active_row, active_col)
    active_col = int((x+150)//35)
    active_row = int((150-y)//35)
    x_fill = active_col*35 - 150
    y_fill = 150 -(active_row)*35
    if 0 <= active_row <= 8 and 0 <= active_col <= 8:
        if grid0[active_row][active_col] == 0:
            myPen.color("#56f321")
            myPen.pensize(2)
            myPen.goto(x_fill, y_fill)
            myPen.pendown()
            
            for i in range(4):
                myPen.forward(35)
                myPen.right(90)
            myPen.penup()
            number = int(float(turtle.numinput("Sudoku", "Choose Number", 1, 1, 9)))
            grid[active_row][active_col] = number
            myPen.clear()
            drawGrid()
            drawnum(grid)
    return
def deactivate_box(active_row, active_col):
    x_fill = active_col*35 - 150
    y_fill = 150 -(active_row)*35
    if 0 <= active_row <= 8 and 0 <= active_col <= 8: 
        myPen.pensize(2)
        myPen.color("#000000")
        myPen.goto(x_fill, y_fill)
        myPen.pendown()
        for n in range(4):
            myPen.forward(35)
            myPen.right(90)
        myPen.penup()
    return

def play_game(grid):
    drawGrid()
    drawnum(grid)
    turtle.onscreenclick(activate_box)
    text("Press Spacebar to solve", -110, -210, 20)
    turtle.onkeypress(h1, "space")
    turtle.listen()
    turtle.mainloop()
play_game(grid)