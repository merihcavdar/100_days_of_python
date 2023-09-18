numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]

print(new_numbers)

name = "Merih"
letter_list = [letter.lower() for letter in name]
print(letter_list)

new_list = [n*2 for n in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5 ]

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)