# 10/5/19 Exercise 5-6: Using if-elif-else chain
# To determine the age and stage of life.
age = 33

if age < 2:
    stage_of_life = 'baby'
elif age <= 2 or age < 4:
    stage_of_life = 'toddler'
elif age <= 4 or age < 13:
    stage_of_life = 'kid'
elif age <= 13 or age < 20:
    stage_of_life = 'teenager'
elif age <= 20 or age < 65:
    stage_of_life = 'adult'
elif age >= 65:
    stage_of_life = 'elder'
print(f"Judging by your age, your stage of life is {stage_of_life}.")
