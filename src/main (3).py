space = 0
ship = [3,4,5]
hit = []
miss = []
guess = hit + miss

def place_shot(guess):
  s = 'yes'
  while s == 'yes':
    try:
      shot = int(input('Guess a shot from 0-99: '))
      if shot < 0 or shot > 99:
        print('Bad number try again')
      elif shot in guess:
        print('Used try again')
      else:
        s = 'no'
        break
    except:
        print('Bad input try again')
  return shot

def check_shot(ship, hit, miss):
    if shot in ship:
      hit.append(shot)
    else:
      miss.append(shot)
    return hit, miss
  
def create_grid(ship, miss, hit, space):
    print('  A B C D E F G H I J')
    for x in range(10):
      row = ""
      for y in range(10):
          board = "_ "
          if space in miss:
            board = 'o '
          elif space in hit:
            board = 'x '
          elif space in ship:
            board = '. '
          row = row + board
          space = space + 1
      print(x,row)

start = True
while start:
  try:
    i = int(input('Welcome to Battleship! To start press 1 : '))
    if i == 1:
      start = False
      break
  except:
      print('Bad input try again')
if i == 1:
  for i in range(10):
    shot = place_shot(guess)
    hit,miss = check_shot(ship, hit, miss)
    create_grid(ship, hit, miss, space)
