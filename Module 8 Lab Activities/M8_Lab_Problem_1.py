# Edward Jimenez
# 11/29/22
# Write a function that takes two inputs from a user and prints whether they are
# equal or not

def compare():
    input1 = int(input("Enter any number: "))
    input2 = int(input("Enter any number: "))

    if input1 == input2:
        print("Both inputs are equal to each other")
    else:
        print("Both inputs are not equal to each other")


compare()
