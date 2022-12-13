# Main_character.py
# Author: Edward Jimenez
# Date: 12/13/22
# Description: This file contains the attributes and properties of the main character in the adventure game.

class enemy_character:
    # Player's attributes
    name = "Enemy"
    hit_points = 100

    def __init__(self, name, hit_points):
        self.hit_points = hit_points
        self.name = name

    def pain(self, pain):
        self.hit_points -= pain

        print("Enemy has taken", pain, "hit_points")


global Enemy
Enemy = enemy_character("Enemy", 100)
