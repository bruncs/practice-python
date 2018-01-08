"""
  Exercise 6
"""
# pylint: disable=invalid-name

a = input("Input a string: ")
if a[::-1] == a:
    print("This is a fucking palindrome!")
else:
    print("This is ain't shit.")
