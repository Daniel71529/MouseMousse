class Enemy:
  def __init__(self, health, attack, defense, name):
    self.health = health
    self.attack_power = attack
    self.defense = defense
    self.name = name

  def attacking(self, mouse):
    damage = self.attack_power - mouse.defense
    mouse.health -= damage
    mouse.health = max(mouse.health, 0)