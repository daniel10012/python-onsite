import random
import time

class Hero:

    def __init__(self, name, strenght, health = 100):
        self.name = name
        self.strenght = strenght
        self.health = health

    def __str__(self):
        return(f"your hero {self.name} has an strenght of {self.strenght} and a health level of {self.health}")

    def attack(self, opponent):
        print("you chose to attack !")
        hero_hand = random.randint(1,10)*self.strenght
        opponent_hand = random.randint(1,10)*opponent.strenght
        print(f"your hand is {hero_hand} while {opponent.name} has {opponent_hand}")
        if hero_hand >= opponent_hand:
            print("you won the fight!, let's continue the quest")
        else:
            self.health -= 30
        #put something for subclasses here


    def lookaround(self):
        print("you chose to look around !")
        outcome = random.choice(["positive", "negative"])
        if outcome == "positive":
            print("good news you found some healing potion and get +10 health!")
            self.health+=10
        else:
            print("bad news, you fell into a monster trap and your health decrease by 10")
            self.health -= 10
        print(f"your health is now {self.health}")

class Opponent:

    def __init__(self,name, strenght):
        self.name = name
        self.strenght = strenght

    def __str__(self):
        return(f"your opponent {self.name} has an strenght of {self.strenght}")


class Alien(Opponent):

    def __init__(self, name, strenght,pulverize):
        super().__init__(name, strenght)
        self.pulverize = "pulverize"


class Zombie(Opponent):

    def __init__(self, name, strenght, eat):
        super().__init__(name, strenght)
        self.bite = "eats"

class Vampire(Opponent):

    def __init__(self, name, strenght, suckblood):
        super().__init__(name, strenght)
        self.suckblood = "sucks blood"













