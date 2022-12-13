# Section_5.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the fifth section of the adventure game.

import main_character
import enemy_character


def start():
    # Print section introduction
    print(
        "You and the sorcerer stand facing each other, ready to fight")

    # Ask player to choose an action
    choice = input("Enter [a] to attack, or [b] to defend: ")

    # Check player's choice and respond
    if choice.lower() == "a":
        print("You charge towards the sorcerer, sword in hand, and attack")
        for i in range(99):
            enemy_character.Enemy.hit_points = 115
            print("The enemy took", main_character.You.pain(1))
            print("His health is now", main_character.You.hit_points)
        print("The sorcerer has died. You have won the game and reached the kingdom, congratulations.")

    elif choice.lower() == "b":
        print("You raise your shield and prepare to defend against the sorcerer's attack")
        while True:
            print("You defended so much that your shield broke and the enemy sliced you into a million pieces")

    else:
        print("\nInvalid choice. Please try again.\n")
        start()
