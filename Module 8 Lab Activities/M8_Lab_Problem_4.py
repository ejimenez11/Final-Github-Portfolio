# Edward Jimenez
# 11/29/22
# Write a function that takes a year as a parameter and returns True if the year is a
# leap year, False if it is otherwise.
# Consider the requirements of a leap year:
# - The year is evenly divisible by 4
# - If the year can be evenly divided by 100 it is NOT a leap year, unless:
# o If the year is also evenly divisible by 400, then it is a leap year.

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

        else:
            return True
    else: return False
print(isLeapYear(2024))
