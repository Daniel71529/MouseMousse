space = 0
ship = [3,4,5]
hit = []
miss = []
guess = hit + miss

def place_shot():
  global guess
  shotY = 'yes'
  while shotY == 'yes':
    try:
      shot = int(input('Guess a shot from 0-99: '))
      if shot < 0 or shot > 99:
        print('Bad number try again')
      elif shot in guess:
        print('Used try again')
      else:
        shotY = 'no'
        break
    except:
        print('Bad input try again')
  return shot

def check_shot():
    global ship
    global hit
    global miss
    if shot in ship:
      hit.append(shot)
    else:
      miss.append(shot)
    return hit, miss
  
def create_grid():
    global ship
    global miss
    global hit
    global space
    print(' A B C D E F G H I J')
    for x in range(10):
      row = ""
      for y in range(10):
          board = "_ "
          if space in miss:
            board = '0 '
          elif space in hit:
            board = 'X '
          elif space in ship:
            board = '. '
          row = row + board
          space = space + 1
      print(x,row)


start = int(input('Welcome to Battleship! To start press 1 : '))
if start == 1:
  for i in range(10):
    shot = place_shot()
    hit,miss = check_shot()
    create_grid()
