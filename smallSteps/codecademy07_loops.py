# Loop review
single_digits = range(0, 10)
print(single_digits)

squares = []

for num in single_digits:
  print(num)
  squares.append(num**2)

print(squares)

cubes = [num**3 for num in single_digits]
print(cubes)