# Section_2.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the second section of the adventure game.

import main_character
import section_3


def start():
    # Print section introduction
    print("As you travel, you realize you should be preparing for any obstacles that might come your way. You take a "
          "moment to decide what to do")

    # Ask player to choose an action
    choice = input("Enter [a] to gather resources, [b] to continue traveling, or [c] scout the area for potential "
                   "dangers: ")

    # Check player's choice and respond
    if choice.lower() == "a":
        print("\nYou look for resources to sustain yourself on your journey.\nYou come across a nearby pond with "
              "berry bushes growing around it.\nYou quickly gather as many berries as you can and then fill your "
              "water bottles from the pond.\nYou continue on your quest to the kingdom, feeling energized and ready "
              "for whatever comes your way.\n")
        print("Press any key to continue")
        input()
        # Start section 3
        section_3.start()

    elif choice.lower() == "b":
        print("\nYou continue your travel towards the kingdom and set your sights on the distant horizon, determined "
              "to reach it as quickly as possible.\nAs the hours pass, you draw closer and closer to the kingdom, "
              "feeling hopeful and excited for what lies ahead.\n")
        print("Press any key to continue")
        input()
        # Start section 3
        section_3.start()

    elif choice.lower() == "c":
        print("\nYou carefully survey your surroundings looking for any signs of danger\nAfter a while, you feel "
              "confident that you've spotted the most dangerous areas and have a plan to avoid them.\nYou continue on "
              "your journey, feeling more prepared now to face whatever comes your way.\n")
        print("Press any key to continue")
        input()
        # Start section 3
        section_3.start()

    else:
        print("\nInvalid choice. Please try again.\n")
        start()

    # Start section 3
    section_3.start()
