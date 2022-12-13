# Section_3.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the third section of the adventure game.

import main_character
import section_4
import random


def start():
    # Print section introduction
    print(
        "You continue your travel through the woods, remaining alert and prepared. As you walk, you hear rustling "
        "nearby, and suddenly, a giant spider reveals itself and stands in front of you, ready to attack")

    # Ask player to choose an action
    choice = input("Enter [a] to attack the spider, [b] to try to talk to it, or [c] to run away, or [d] to use your "
                   "magic to defend yourself: ")

    # Check player's choice and respond
    if choice.lower() == "a":
        # Roll the dice to determine if player is successful in defeating the spider
        if random.random() < 0.5:
            print(
                "\nYou attack the spider with your weapon, trying to defeat it.\nThe spider strikes back with powerful "
                "blows, but you are able to hold your own and fight back.\nAfter a fierce battle, you emerge "
                "victorious, feeling proud of your strength and skill.\n")
            print("Press any key to continue")
            input()
            # Start section 4
            section_4.start()
        else:
            print(
                "\nYou attack the spider with your weapon, but it proves too powerful for you to defeat.\nThe spider "
                "overpowers you, and you are unable to continue on your journey. The game ends here.\n")
            print("Press any key to continue")
            input()
            # Restart section 3
            start()

    elif choice.lower() == "b":
        # Roll the dice to determine if player is successful in talking to the spider
        if random.random() < 0.5:
            print("\nYou try to talk to the spider, hoping to find a peaceful resolution.\nThe spider seems confused "
                  "by your words, and hesitates for a moment before attacking.\nYou were able to dodge its blows, "
                  "and continue talking to it in a soothing voice.\nAfter a few minutes, the spider calms down and "
                  "retreats, leaving you unharmed.\n")
            print("Press any key to continue")
            input()
            # Start section 4
            section_4.start()
        else:
            print("\nYou try to talk to the spider, but it is not interested in hearing your words.\nIt attacks you, "
                  "and you are unable to escape from its clutches. The game ends here.\n")
            print("Press any key to continue")
            input()
            # Restart section 3
            start()

    elif choice.lower() == "c":
        # Roll the dice to determine if player is successful in running away from the spider
        if random.random() < 0.5:
            print("\nYou quickly turn around and run away from the spider, trying to escape from danger.\nYou run as "
                  "fast as you can, dodging branches and leaping over rocks.\nAfter a few minutes you see the spider "
                  "in the distance as it gives up on the chase.\nYou continue on your journey, feeling relieved.\n")
            print("Press any key to continue")
            input()
            # Start section 4
            section_4.start()
        else:
            print("\nYou try to run away from the spider, but it is too fast for you to escape.\nThe spider catches "
                  "up and bites you, injecting its venom into your body.\nYou are unable to continue on your journey, "
                  "and the game ends here.\n")
            print("Press any key to continue")
            input()
            # Restart section 3
            start()

    elif choice.lower() == "d":
        # Roll the dice to determine if player is successful in running away from the spider
        if random.random() < 0.5:
            print("\nYou use your magic to create a protective shield around yourself, and the spider's attacks "
                  "bounce off of it harmlessly.\nYou are able to keep the shield long enough to weaken the spider, "
                  "and it eventually retreats, leaving you unharmed.\nYou continue on your journey, feeling grateful "
                  "for your magic abilities.\n")
            print("Press any key to continue")
            input()
            # Start section 4
            section_4.start()
        else:
            print("\nYou try and use your magic to defend yourself against the spider, but the spell is not strong "
                  "enough to protect you.\nThe spider overpowers you, and you are unable to continue on your journey. "
                  "The game ends here.\n")
            print("Press any key to continue")
            input()
            # Restart section 3
            start()

    else:
        print("Invalid choice. Please try again.")
        start()

    # Start section 4
    section_4.start()
