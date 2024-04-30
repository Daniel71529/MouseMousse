
from mouse import Mouse
from enemy import Enemy
from weapon import Weapon
from item import Item

mouse1 = Mouse(100, 10, 10, 'Harvest Mouse')
mouse2 = Mouse(200, 20, 15, 'New York Rat')
mouse3 = Mouse(500, 30, 5, 'Rat King')
enemy1 = Enemy(20, 15, 3, 'Ant')
item1 = Item('health', 30, 0, 0)

def inv():
  f = open('inventory.txt', 'r')
  print(f.read())

def stats():
  print('Health:', mouse1.health, '|', 'Attack:', mouse1.attack_power, '|', 'Defense:', mouse1.defense)

def main_path():
  i = int(input('\nYou stand at a fork in the path, go left or right? \nEnter 1 to see your stats, 2 for left, 3 for right: '))
  if i == 1:
    stats()
    main_path()
  elif i == 2:
    print('You go left and find a dude!')
    p = int(input('He has a sword, do you want to fight him? 1 for yes, 2 for no: '))
    if p == 1:
      battle()
    elif p == 2:
      print('You run away and find a potion!')
  elif i == 3:
    print('You go right and encounter an enemy!')
    battle()
  
def mouseselect():
  while True:
    try:
      print('Difficulty Easy: Rat King', '|', 'Health', mouse3.health, '|', 'Attack', mouse3.attack_power, '|', 'Defense', mouse3.defense)
      print('Difficulty Medium: New York Rat', '|', 'Health', mouse2.health, '|', 'Attack:', mouse2.attack_power, '|', 'Defense:', mouse2.defense)
      print('Difficulty Hard: Harvest Mouse', '|', 'Health:', mouse1.health, '|', 'Attack:', mouse1.attack_power, '|', 'Defense:', mouse1.defense)
      
      
      s = int(input('Select your mouse: '))
      if s == 1:
        print('You have selected Harvest Mouse!')
        return mouse1
      elif s == 2:
        print('You have selected New York Rat!')
        return mouse2
      elif s == 3:
        print('You have selected Rat King!')
        return mouse3
    except:
      print('Please select a valid mouse!')

def battle():
  print('\nYou have encountered an enemy!')
  Yes = True
  print('1: Attack')
  print('2: Equip Weapon')
  print('3: Consume Item')
  print('4: Run')
  while True:
    try:
      choice = int(input('\nWhat will you do? '))
      if choice == 1:
        selected_mouse.attack(enemy1)
        print('You attacked the enemy!')
        enemy1.attacking(selected_mouse)
        print('The enemy attacked you!')
        print('Your health:', selected_mouse.health)
        print('Enemy health:', enemy1.health)
        if selected_mouse.health == 0:
          print('You died!')
          break
        if enemy1.health == 0:
          print('You won!')
          enemy1.health = 40
          break
      elif choice == 2:
          weapon = Weapon('Sword', 10)
          selected_mouse.equip(weapon)
          battle()
      elif choice == 3:
        item1.drink(selected_mouse)
        battle()
      elif choice == 4:
        enemy1.attacking(selected_mouse)
        print('The enemy attacked you!')
        print('You ran away!')
        print('Your health:', selected_mouse.health)
        break
    except:
      print('Bad input try again')
  
start = True
while start:
  try:
    i = int(input('Welcome to MouseMousse! To start press 1 : '))
    if i == 1:
      start = False
  except:
      print('Bad input try again')
selected_mouse = mouseselect()
name = input('You are a ' + selected_mouse.name + '. What is your name? ')
print(name, 'is a great name!')
print('\nYou have been cursed by the evil rat champion and you must find the legendary mouse mousse to save your kingdom. You start your journey at the base of the mountain and must climb up to face the champion.')
f = open('inventory.txt', 'w')
f.close
inv()
main_path()






