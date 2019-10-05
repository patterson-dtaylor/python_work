# 9/29/19 Constructing my first list. Remember, the index starts at 0 not 1.
# Also, -1 indicates the last item on the list
# While -2 indicates the second to last item on the list (-3 etc.).
bicycles = ['trek', 'cannondale',
                    'redline', 'specailized', ]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3].title())
print(bicycles[-1])
message = f"My favorite bicycle was a {bicycles[0].title()}."
print(message)
