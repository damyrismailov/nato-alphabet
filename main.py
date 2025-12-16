import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

pho_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Press enter word\n").upper()
    try:
        final_d = [pho_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letter in the alphabet please')
        generate_phonetic()
    else:
        print(final_d)
generate_phonetic()


