class Item:
  def __init__(self, type, amount_health, amount_defense, amount_attack):
    self.type = type
    self.amount_health = amount_health
    self.amount_attack = amount_attack
    self.amount_defense = amount_defense

  def drink(self, mouse): 
    if self.type == 'health':
      mouse.health += self.amount_health
      print('You drank the potion and gained', self.amount_health , 'health!')
    elif self.type == 'attack':
      mouse.attack_power += self.amount_attack
      print('You drank the potion and gained', self.amount_attack , 'attack!')
    elif self.type == 'defense':
      mouse.defense += self.amount_defense
      print('You drank the potion and gained', self.amount_defense , 'defense!')
    