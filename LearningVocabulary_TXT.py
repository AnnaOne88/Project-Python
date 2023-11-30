import random

file_path = 'C:/Users/Uzivatel/Desktop/vocabulary.txt' #your path to TXT file

# Open the file and read lines into a list
with open(file_path, 'r') as file:
    words_list = file.read().splitlines()

# Print the list of words
print("Vocabulary:", words_list)

random_word = random.choice(words_list)
print("Random Word from Vocabulary:", random_word)