# 10/1/19 Using range with squares from numbers 1 through 10.
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)
