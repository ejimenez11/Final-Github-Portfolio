# Edward Jimenez
# 11/1/22

# Creates a range from numbers 1-50 and determines if they are divisible by 3 and/or 5

for numbers in range(1, 51):
    if numbers % 3 and numbers % 5 == 0:
        print("Divisible by 3 & 5")

    elif numbers % 3 == 0:
        print("Divisible by 3")
    elif numbers % 5 == 0:
        print("Divisible by 5")

    else:
        print("\n", numbers)
