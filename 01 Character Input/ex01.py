"""
  Exercise 1
"""
# pylint: disable=invalid-name

name = input("What's your name? ")
age = int(input("How old are you? "))
copies = int(input("How many copies do you want to see? "))
year = str(100 - age + 2018)
print(copies * ("Your name is " + name + " and you will turn 100 years old in " + year + ".\n"))
