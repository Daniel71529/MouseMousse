class Mouse:
  def __init__(self, health, attack, defense, name):
    self.health = health
    self.attack_power = attack
    self.defense = defense
    self.name = name
    
  def attack(self, enemy):
    damage = self.attack_power - enemy.defense
    enemy.health -= damage
    enemy.health = max(enemy.health, 0)

  def equip(self, weapon):
    self.weapon = weapon
    self.attack_power += weapon.damage
    print('You equipped', weapon.name, 'your attack is now: ', self.attack_power)
  

  
