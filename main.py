import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("Pick your word: ").upper()
    try:
        output_list = [nato_dict[letters] for letters in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
