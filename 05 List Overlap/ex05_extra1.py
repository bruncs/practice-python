"""
  Exercise 5 Extra 1
"""
# pylint: disable=invalid-name
import random

# random.sample(population, 5) uma lista de 5 elementos escolhidos da população,
# que no caso é dada por range(10), ou seja, números de 0 a 9.

a = random.sample(range(10), 5)
b = random.sample(range(10), 5)
commonElements = []

for element in a:
    if element in b and not element in commonElements:
        commonElements.append(element)
print("a = " + str(a))
print("b = " + str(b))
print("Common elements = " + str(commonElements))
