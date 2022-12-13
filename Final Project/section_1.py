# Section_1.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the first section of the adventure game.

import main_character
import section_2


def start():
    # Print section introduction
    print(
        "You find yourself in a cave where you slept for the night. It's now morning and you must continue your "
        "journey to the kingdom")

    # Ask player to choose an action
    choice = input("Enter [a] to leave the cave, [b] to gather information, or [c] to stay in the cave): ")

    # Check player's choice and respond
    if choice.lower() == "a":
        print("\nYou decide to leave the cave.\nAs you make your way through the cave, you come cross a group of "
              "travelers who are heading in the same direction.\nThey invite you to join them, and you gladly accept, "
              "knowing it is safer in numbers.\nTogether, you continue your path to the kingdom, sharing stories along "
              "the way.\n")
        print("Press any key to continue")
        input()
        # Start section 2
        section_2.start()

    elif choice.lower() == "b":
        print("\nYou look around the cave and gather some extra information.\nAfter looking around the cave, "
              "you see some dangerous-looking monsters lurking in the shadows.\nSensing it wasn't safe to be in there "
              "any longer, you quickly gathered your belongings and made your way out of the cave.\n")
        print("Press any key to continue")
        input()
        # Start section 2
        section_2.start()

    elif choice.lower() == "c":
        print("\nYou decide to stay in the cave for a while.\nAs you explore the cave, you come across a hidden "
              "passage that leads to a secret chamber.\nInside the chamber, you find a treasure chest filled with "
              "valuables.\nYou quickly gather as much as you can carry and continue on your journey to the kingdom, "
              "feeling grateful for the unexpected discovery.\n")
        print("Press any key to continue")
        input()
        # Start section 2
        section_2.start()

    else:
        print("\nInvalid choice. Please try again.\n")
        start()

    # Start section 2
    section_2.start()
