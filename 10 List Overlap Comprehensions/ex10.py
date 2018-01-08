"""
  Exercise 10
"""
# pylint: disable=invalid-name

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = [element for element in set(a) if element in b] # A função set() remove os duplicados.
print(overlap)
