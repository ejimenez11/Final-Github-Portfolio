#Edward Jimenez
#12/10/22
#Problem 4
# Create a while loop that initializes a counter at 0 and will run until the counter
# reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement.

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("The values that are divisible by 10 are: ", tens)
