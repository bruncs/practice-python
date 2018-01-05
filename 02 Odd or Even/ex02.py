"""
  Exercise 2
"""
# pylint: disable=invalid-name

number = int(input("Input a number: "))
check = int(input("Input a divisor number: "))

# Se é par
if number % 2 == 0:
    if number % check == 0:
        print("This is a beautiful even number, and " + str(check) +
              " divides evenly into " + str(number) + "!")
    else:
        print("This is a beautiful even number, but " + str(check) +
              " does not divide evenly into " + str(number) + "!")

# Se é ímpar
else:
    if number % check == 0:
        print("This is a fucking odd number, and " + str(check) +
              " divides evenly into " + str(number) + "!")
    else:
        print("This is a fucking odd number, and " + str(check) +
              " does not divide evenly into " + str(number) + "!")
