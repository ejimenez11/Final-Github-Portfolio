# Edward Jimenez
# 11/28/22
# Write a Python function to multiply all the numbers in a list. The function should
# take a list of numbers as a parameter and return the final result of the multiplication.

def num(list):
    output = 1
    for number in list:
        output = output * number
    return output


num_list = [1, 2, 3, 4, 5]
print(num(num_list))
