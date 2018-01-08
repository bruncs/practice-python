"""
  Exercise 6
"""
# pylint: disable=invalid-name

str = input("Input a string: ")
if str[::-1] == str:
  print("This is a fucking palindrome!")
else:
  print("This is ain't shit.")
