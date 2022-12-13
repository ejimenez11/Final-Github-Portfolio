# Section_4.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the fourth section of the adventure game.

import main_character
import enemy_character
import section_5
import random


def start():
    # Print section introduction
    print("As you reach the final stretches of your journey, you come across a man who claims to be a sorcerer, "
          "and can offer you a lead to the kingdom for a small fee. You remain very wary of his intentions, "
          "but you must decide what to do")

    # Ask player to choose an action
    choice = input("Enter [a] to accept the sorcerer's offer, [b] to reject the sorcerer's offer: ")

    # Check player's choice and respond
    if choice.lower() == "a":
        # Roll the dice to determine if player is successful in dodging/landing the attack
        if random.random() < 0.5:
            print("\nYou accept the sorcerer's offer and pay the fee.\nThe sorcerer leads you to a hidden passageway "
                  "that takes you directly to the kingdom.\nHowever, as you reach the kingdom gates, he suddenly "
                  "tries to attack you.\nYou are able to anticipate his attack and dodge it, successfully landing a "
                  "counter-attack that injures the sorcerer")
            enemy_character.Enemy.hit_points = 100
            print("The enemy took", main_character.You.pain(random.randint(10, 25)))
            print("His health is now", main_character.You.hit_points)
        else:
            print("\nYou accept the sorcerer's offer and pay the fee.\nThe sorcerer leads you to a hidden passageway "
                  "that takes you directly to the kingdom.\nHowever, as you reach the kingdom gates, he suddenly "
                  "tries to attack you.\nYou are not able to anticipate his attack and he hits you, causing you to "
                  "take some damage.")
            main_character.You.hit_points = 100
            print("You took", main_character.You.pain(random.randint(10, 25)))
            print("Your health is", main_character.You.hit_points)
        # Start section 5
        section_5.start()

    if choice.lower() == "b":
        # Roll the dice to determine if player is successful in dodging/landing the attack
        if random.random() < 0.5:
            print("\nYou reject the sorcerer's offer and continue on your journey.\nAs you approach the kingdom "
                  "gates, the sorcerer ambushes you.\nYou are able able to anticipate his attack and dodge it, "
                  "successfully landing a counter-attack that injures the sorcerer")
            enemy_character.Enemy.hit_points = 100
            print("The enemy took", main_character.You.pain(random.randint(10, 25)))
            print("His health is now", main_character.You.hit_points)
        else:
            print("\nYou reject the sorcerer's offer and continue on your journey.\nAs you approach the kingdom "
                  "gates, the sorcerer ambushes you.\nYou are not able to anticipate his attack and he hits you, "
                  "causing you to take some damage.")
            main_character.You.hit_points = 100
            print("You took", main_character.You.pain(random.randint(10, 25)))
            print("Your health is", main_character.You.hit_points)
        # Start section 5
        section_5.start()
    else:
        print("\nInvalid choice. Please try again.\n")
        start()

    # Start section 5
    section_5.start()
