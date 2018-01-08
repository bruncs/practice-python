"""
  Exercise 7
"""
# pylint: disable=invalid-name

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

# Do jeito tradicional:
for element in a:
    if element % 2 == 0:
        b.append(element)

# Em uma linha só:
c = [item for item in a if item % 2 == 0]

# Imprimindo dos dois jeitos:
print(b)
print(c)
