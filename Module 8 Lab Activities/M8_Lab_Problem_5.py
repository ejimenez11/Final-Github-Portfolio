# Edward Jimenez
# 11/29/22
# Given the following working code:
# Write a function that checks whether your game character has picked up all the items needed
# to perform certain tasks and checks against any status debuffs. Confirm checks with print
# statements.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


    def task1(player):
        if 'rope' in player1.weapons and 'coat' in player1.weapons and 'first aid kid' in player1.weapons and 'slow' not in player1.weaknesses:
            return True
        else:
            return False


    def task2(player):
        if 'pan' in player1.weapons and 'groceries' in player1.weapons and 'small' not in player1.weapons:
            return True
        else:
            return False


    def task3(player):
        if "pen" in player1.weapons and 'paper' in player1.weapons and 'idea' in player1.weapons and 'confusion' not in player1.weaknesses:
            return True
        else:
            return False

if task1(player1):
    print("You can climb a mountain")

if task2(player1):
    print("You can cook a meal")
if task3(player1):
    print("You can write a book")