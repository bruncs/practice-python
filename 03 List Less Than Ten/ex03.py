numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbersLessThan5 = []

for number in numbers:
  if number < 5:
    numbersLessThan5.append(number)

print(str(numbersLessThan5))

# Extra
print("\nExtra Print: ")
print([element for element in [1,1,2,3,6,8,13,21,34,55,89] if element < 5])
