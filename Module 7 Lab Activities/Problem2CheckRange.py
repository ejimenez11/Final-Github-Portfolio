# Edward Jimenez
# 11/28/22
# Write a Python function to check whether a number is between 1 and 10. The
# function should take a number as a parameter and return True if the number is between 1 and
# 10, and False if the number is not between 1 and 10

def number(check):
    if check < 1:
        return False
    if check > 10:
        return False
    else:
        return True


input = int(input("Input any number \n"))
output = number(input)
print(output)
