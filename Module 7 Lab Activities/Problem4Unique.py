# Edward Jimenez
# 11/28/22
# Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list. Use the append() function.

def list(num):
    list = []
    for x in num:
        if x not in list:
            list.append(x)
    return list


print(list([1, 3, 3, 3, 6, 2, 3, 5]))
