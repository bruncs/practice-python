"""
  Exercise 4
"""
# pylint: disable=invalid-name

number = int(input("Input a number: "))
checkList = range(1, number)

print([check for check in checkList if number % check == 0])
