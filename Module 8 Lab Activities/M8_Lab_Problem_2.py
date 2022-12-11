# Edward Jimenez
# 11/29/22
# Write a function that takes two inputs from a user and prints whether the sum is
# greater than 10, less than 10, or equal to 10

def sum():
    input1 = int(input("Enter any number: "))
    input2 = int(input("Enter any number: "))

    if input1 + input2 > 10:
        print("The sum of both numbers is GREATER THAN 10")
    if input1 + input2 < 10:
        print("The sum of both number is LESS THAN 10")
    if input1 + input2 == 10:
        print("The sum of both numbers is EQUAL to 10")


sum()