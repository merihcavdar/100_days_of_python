import pandas

data = pandas.read_csv("nato_phonetic.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


is_valid = False


def check_validity(word):
    for w in word:
        if w not in phonetic_dict.keys():
            global is_valid
            is_valid = False
            raise KeyError


while not is_valid:
    try:
        word = input("Enter a word: ").upper()
        check_validity(word)
    except KeyError:
        print("must contain only letters")
    else:
        is_valid = True


output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
