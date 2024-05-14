from mouse import Mouse
from enemy import Enemy
from weapon import Weapon
from item import Item

inv = []
mouse1 = Mouse(100, 10, 10, 'Harvest Mouse')
mouse2 = Mouse(200, 20, 15, 'New York Rat')
mouse3 = Mouse(500, 30, 5, 'Rat King')
dude = Enemy(40, 20, 3, 'Dude')
bird = Enemy(20, 30, 3, 'Bird')
rock = Enemy(100, 0, 0, 'Rock')
rat_king = Enemy(100, 20, 3, 'Rat King')
health_item = Item('health', 30)
sword = Weapon('Sword', 10)

def weapon_inv(weapon):
  inv.append(weapon)
  print('You picked up', weapon.name)
  
def item_inv(item):
  inv.append(item)
  print('You picked up', item.type)

def display_inv():
  if inv == []:
    print('Inventory is empty')
  else:
    for i in inv:
      print(i.name)


def main_path():
  while True:
    try:
      choice1 = int(input('\nYou stand at a fork in the path, go left or right? \nEnter 1 for left, 2 for right: '))
      if choice1 == 1:
        print('You go left and find a dude!')
        choice2 = int(input('He has a sword, do you want to fight him? 1 for yes, 2 for no: '))
        if choice2 == 1:
          battle(dude)
          weapon_inv(sword)
          continued()
          break
        elif choice2 == 2:
          print('You run away and find a potion!')
          item_inv(health_item)
          continued2()
          break
      elif choice1 == 2:
        print('You go right and encounter an enemy!')
        battle(dude)
        continued2()
    except:
      print('Bad input, try again')

def continued():
  while True:
    try:
      print('\nYou continue on the path')
      print('You encounter big rock')
      choice3 = int(input('Do you want to fight it? 1 for yes, 2 for no: '))
      if choice3 == 1:
        battle(rock)
        print('The magical rock heals you and disappears')
        ending()
        break
      elif choice3 == 2:
        print('The rock tumbles down and squashes you')
        selected_mouse.health -= 50
        print('Your health: ',selected_mouse.health)
        ending()
        break
    except:
        print('Bad input, try again')

def continued2():
    while True:
      try:
        print('\nYou continue on the path')
        print('You encounter a bird')
        choice4 = int(input('Do you want to fight it? 1 for yes, 2 for no: '))
        if choice4 == 1:
          battle(bird)
          print('The bird disappears and you find a potion!')
          item_inv(health_item)
          ending()
          break
        elif choice4 == 2:
          print('The bird flies away and you find a potion!')
          item_inv(health_item)
          ending()
          break
      except:
        print('Bad input, try again')

def ending():
    while True:
      try:
        print('\nYou reached the top of the mountain, he is waiting')
        print('You encounter the rat king')
        print('You must fight')
        battle(rat_king)
        break
      except:
        print('Bad input, try again')


def mouseselect():
  while True:
    try:
      print('Difficulty Easy: Rat King', '|', 'Health', mouse3.health, '|', 'Attack', mouse3.attack_power, '|', 'Defense', mouse3.defense)
      print('Difficulty Medium: New York Rat', '|', 'Health', mouse2.health, '|', 'Attack:', mouse2.attack_power, '|', 'Defense:', mouse2.defense)
      print('Difficulty Hard: Harvest Mouse', '|', 'Health:', mouse1.health, '|', 'Attack:', mouse1.attack_power, '|', 'Defense:', mouse1.defense)     
      s = int(input('Select your mouse with 1, 2, or 3: '))
      if s == 3:
        print('You have selected Harvest Mouse!')
        return mouse1
      elif s == 2:
        print('You have selected New York Rat!')
        return mouse2
      elif s == 1:
        print('You have selected Rat King!')
        return mouse3
    except:
      print('Please select a valid mouse!')

def battle(enemy):
  print('\nYou have encountered an enemy!')
  print('1: Attack')
  print('2: Equip Weapon')
  print('3: Consume Item')
  print('4: Run')
  while True:
    try:
      choice = int(input('\nWhat will you do? '))
      if choice == 1:
        selected_mouse.attack(enemy)
        print('You attacked the enemy!')
        enemy.attacking(selected_mouse)
        print('The enemy attacked you!')
        print('Your health:', selected_mouse.health)
        print('Enemy health:', enemy.health)
        if selected_mouse.health == 0:
          print('You died!')
          break
        if enemy.health == 0:
          print('You won!')
          dude.health = 40
          bird.health = 20
          rock.health = 100
          rat_king.health = 100
          break
      elif choice == 2:
        if sword in inv:
          selected_mouse.equip(sword)
          inv.remove(sword)
        else:
          print('Inventory empty')
          battle(enemy)
      elif choice == 3:
        if health_item in inv:
          health_item.drink(selected_mouse)
          inv.remove(health_item)
        else:
          print('Inventory empty')
          battle(enemy)
      elif choice == 4:
        if enemy == rat_king:
          print("You can't do that")
        else:
          enemy.attacking(selected_mouse)
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
print('\nYou have been cursed by the evil rat king and you must find the legendary mouse mousse to save your kingdom. You start your journey at the base of the mountain and must climb up to face the champion.')
main_path()
print(name, 'has found the legendary mousse from the rat king and is the new ruler of the kingdom!')
print('You have saved the kingdom!')





