# 10/1/19 Exercise 4-7: Make a list of multiples from 3 to 30 and use a for loop to print a list.
multiples = []
for value in range(3, 31):
    multiple = value * 3
# Remember you can add this line or take it out.  Either way it come to the same output.
    multiples.append(multiple)

print(multiples)
