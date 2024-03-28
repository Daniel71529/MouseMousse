
start = int(input('Welcome to Battleship! To start press 1 : '))

if start == 1:
  space = 0

  def create_grid():
    ship = [2,3,4]
    global space
    print(' A B C D E F G H I J')
    for x in range(10):
      row = ""
      for y in range(10):
          board = "_ "
          if space in ship:
            board = '0 '
          row = row + board
          space = space + 1
      print(x,row)
  create_grid()
          
##  def create_grid():
##    grid = [[]]
##    grid_size = 10
##
##    rows, cols = (grid_size, grid_size)
##
##    grid = []
##    for i in range(rows):
##        row = []
##        for j in range(cols):
##          row.append(0)
##        grid.append(row)
##    for row in grid:
##      print(row)
##  create_grid()
