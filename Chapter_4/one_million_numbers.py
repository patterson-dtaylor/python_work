# 10/1/19 Exercise 4-4: Using a for loop to count to 1 million
# Also, fiding the min number, max number, and sum number.
numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
