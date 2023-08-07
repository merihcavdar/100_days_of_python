# mersenne twister
import random
import day4_my_module
# random is a module

random_integer = random.randint(1,10)
print(random_integer)

print(day4_my_module.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")