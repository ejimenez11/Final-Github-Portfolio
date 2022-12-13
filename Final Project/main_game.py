# Main_game.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file is the main game file for the adventure game. It imports and runs the other game sections.

import section_1
import main_character
import random


def start():
    print("Press any key to continue")

    input()

    # Print introduction narration
    print("As the sun begins to set, it grows dark very quickly.\nYou can barely see your hand in front of you, "
          "and start to worry about how you will navigate through the forest, but you have no choice but to continue, "
          "hoping you find shelter before the night grows too cold")
    input()

    print("You approach a mysterious cave, and decide it's best to spend the night there.\nYou notice that it is "
          "dimly light by a small fire. Relieved to have found shelter, you can't shake the feeling that you are "
          "being watched.")
    input()
    # Start section 1
    section_1.start()


# Start the game
start()
