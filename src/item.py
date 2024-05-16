# Daniel Luo
class Item:
  def __init__(self, type, amount_health):
    self.type = type
    self.amount_health = amount_health

  def drink(self, mouse): 
    if self.type == 'health':
      mouse.health += self.amount_health
      print('You drank the potion and gained', self.amount_health , 'health!')
      print('Your health is now', mouse.health)
 
    
