import random

names_string = input("Give me everybody\s names, separated by a comma. ")
names = names_string.split(", ")
print(names)
print(f"the one who will pay the bill is: {names[random.randint(0, len(names)-1)]}")


print(random.choice(names))
