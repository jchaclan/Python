# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
# THIS IS ALSO POSSIBLE ->>> my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]
cat1 = Cat('Freddy', 10)
cat2 = Cat('Manny', 8)
cat3 = Cat('Lucy', 9)

# 2 Create a function that finds the oldest cat


def getOldestCat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


print(
    f'The oldest cat is {getOldestCat(cat1.age, cat2.age, cat3.age)}  years old')
