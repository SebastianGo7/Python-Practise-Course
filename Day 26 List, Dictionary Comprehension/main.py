import pandas
import csv

# This part creates a dictionary which has all the letters and their according words
with open("nato_phonetic_alphabet.csv", mode="r") as alphabet_file:
    content = csv.reader(alphabet_file)
    my_dict = dict((rows[0], rows[1]) for rows in content)
del my_dict["letter"]  # deletes first pair (letter,code), as it is not needed


# this part first asks for a name as an input
# then it iterates through it and adds lists to a list, with the corresponding alphabet words
input_text = (input("Enter your name: ")).upper()

# Alternative with less list comprehension:
# new_list_with_al_words = []
# for letter in input_text:
#     word = (value for (key, value) in my_dict.items() if key == letter)
#     new_list_with_al_words.append(word)

new_list_with_al_words = [[value for (key, value) in my_dict.items() if key == letter] for letter in input_text]
print(new_list_with_al_words)


# solution of course:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)
