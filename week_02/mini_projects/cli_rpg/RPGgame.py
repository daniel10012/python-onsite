import random
from characters import *



def main():
    print_welcome()
    play_game()

def print_welcome():
    print("Welcome to the game ! let's start our quest by entering the Forest..")

def play_game():

    hero = Hero("Bob",10)

    opponents = [
        Vampire("Ming", 3),
        Vampire('Robert', 6),
        Zombie('Martin', 10),
        Zombie('Casey', 20),
        Alien('Fred', 25),
        Alien('Blake', 30)
    ]



    while opponents != []:

        current_opponent = random.choice(opponents)

        print(f"you make your way in the Forest when all of a sudden you come across the "
              f"terrifying {current_opponent.name} who has strenght level of {current_opponent.strenght}")


        action = input("do you want to [a]ttack, [l]ook around or [r]un away?")

        while action not in ["a","l","r","q"]:
            print("please select between letters a,l,r, or press q to quit")
            action = input("do you want to [a]ttack, [l]ook around or [r]un away?")

        if action == "a":
            hero.attack(current_opponent)

        elif action == "l":
            hero.lookaround()
            continue

        elif action == "r":
            print("you run away as far as you can but there are still monsters left:")
            for op in opponents:
                print(f" - {op.name}")
            continue

        elif action == "q":
            print("see you lata quitta !!!")
            break

        opponents.remove(current_opponent)
        if hero.health <= 0:
            print ("YOU DIED")
            break
    if hero.health > 0:
        print("Congratulations you defeated all your opponents !!")


if __name__ == '__main__':
    main()

