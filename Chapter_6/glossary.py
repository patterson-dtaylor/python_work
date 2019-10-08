# 10/6/19 Exercise 6-3: Constructing a glossary of terms.
glossary = {
    'print': 'this allows you print a program',
    'for loop': 'this loop lets you test one item in a list',
    'if statement': 'for every item in a list do this',
    'elif statement': 'stands for else if used between if and else',
    'else statement': 'lets you exend the if statement to else',
    'f function': 'lets you print program with a specific item',
    'dictionary': 'a list of items with a specific key and value',
    'item method': 'allows you loop through all items in a dictionary',
    'key method': 'allows you to loop with only keys',
    'value method': 'allows you to loop with only values',
}

# This is okay, but there is a better way to do things:
# Use loops!
print("Glossary of terms:")
# print(f"\nPrint: {glossary['print']}")
# print(f"\nFor Loop: {glossary['for loop']}")
# print(f"\nIf Statment: {glossary['if statement']}")
# print(f"\nElse Statment: {glossary['else statement']}")
# print(f"\nF Function: {glossary['f function']}")

# 10/6/19 Exercise 6-4 Glossary 2.0
# Using loops to better print the glossary.
for word, definition in glossary.items():
    print(f"{word.title()}: {definition.title()}.")
