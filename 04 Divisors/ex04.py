"""
  Exercise 4
"""
# pylint: disable=invalid-name

number = int(input("Input a number: "))
checkList = range(1, number+1)

print([check for check in checkList if number % check == 0])
