import random
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
    
    
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):   
        self.name = name
        self.health = health
        self.strength = strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return self.name +' '+'has received' + ' ' + str(damage) +' ' + 'points of damage'
        else:
            return self.name + ' ' + 'has died in act of combat'
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        else:
            return 'A Saxon has died in combat'
#War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking) 
        
    def addSaxon(self, Saxon):
            self.saxonArmy.append(Saxon)  
            
    def vikingAttack(self):
        Vik = random.choice(vikingArmy)
        Sax = random.choice(saxonArmy)
        damage_sax = Saxon.receiveDamage(Vik.attack())
        if Saxon.health = 0:
            self.saxonArmy.remove(Sax)
        return damage_sax
            
    def saxonAttack(self):
        Sax = random.choice(saxonArmy)
        Vik = random.choice(vikingArmy)
        damage_vik = Viking.receiveDamage(Sax.attack())
        if Viking.health = 0:
            self.vikingArmy.remove(Vik)
        return damage_vik
                                  
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) == 0:
            return 'Vikings and Saxons are still in the thick of battle.'
        elif len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        
            
            
        
     
        
        