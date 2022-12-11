#Edward Jimenez
#12/10/22
#Problem 3
#Using a while loop, ask the user to enter a number. Append each entered number
#to a list and add them together. Continue asking for a number until the sum of the list of
#numbers is greater than 100

numbers = []
sum = 0

while sum <= 100:
    number = int(input("Enter a number: "))
    numbers.append(number)
    sum += number

print("You entered: ", numbers)
print("The sum of the numbers is: ", sum)
