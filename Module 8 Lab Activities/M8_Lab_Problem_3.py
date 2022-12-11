# Edward Jimenez
# 11/29/22
# Write a function that takes a list and prints if the value 5 is in that list

def five():
    list = []
    numbers = int(input("Enter a list of intergers you plan to input, then the desired numbers : "))

    for i in range(0, numbers):
        num_list = int(input())
        list.append(num_list)
    print(list)

    if 5 in list:
        print("There is a 5 in this list")


five()



