"""
  Exercise 4
"""
# pylint: disable=invalid-name

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonElements = []

for element in a:
    if element in b and not element in commonElements:
        commonElements.append(element)
print(commonElements)
