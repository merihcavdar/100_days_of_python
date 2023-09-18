import pandas

all_letters = {row.letter: row.code for (index, row) in pandas.read_csv("nato_alphabet.csv").iterrows()}

user_input = input("Enter a word: ").upper()

result = {letter: all_letters[letter] for letter in user_input}
print(result)