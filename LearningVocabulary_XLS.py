import openpyxl
import random

#STEP 1: create a function that will read XLS file and create a dictionary of EN-CN pairs.
# Later, we can keep these 'unnecessary' steps in comment mode.

def read_xlsx(path):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    word_dictionary = {} # Dictionary to store English-Chinese words

    for row in sheet.iter_rows(min_row=2, values_only=True):    # this loop adds words into the dictionary, min_row=2 skips the first line (header)
        english_word, chinese_word = row
        word_dictionary[english_word] = chinese_word

    return word_dictionary

path = 'C:/Users/Uzivatel/Downloads/vocabulary-list.xlsx' # the path to your XLSX file

word_dict = read_xlsx(path) # Read the XLSX file and create a dictionary

#STEP 2: let's print the dictionary to check
print("Our Dictionary:")
for english_word, chinese_word in word_dict.items():
    print(f"{english_word}: {chinese_word}")

#STEP 3: let's choose a random key-value pair from the dictionary
random_pair = random.choice(list(word_dict.items()))
random_english_word, random_chinese_word = random_pair
print(f"\nRandom word: {random_english_word} : {random_chinese_word}") #this format can be changed

##STEP 4: Create a list of English words from the keys of the vocabulary dictionary. Use our previous code for interactive revision.
words = list(word_dict.keys())
random_word = random.choice(words)
random.shuffle(words)
#print(random_word)

for word in words:
        print(f"\nWhat is '{word}' in Chinese?")        # Print a prompt asking for the meaning of the current English word. The 'f' before the string indicates the use of an f-string in Python. F-strings, or formatted string literals, were introduced in Python 3.6. They provide a concise and convenient way to embed expressions inside string literals, using curly braces {} to enclose the expressions.
        user_input = input("Your answer: ").strip()   # Take user input for the meaning of the current English word. --- .strip() removes white spaces from the input.
        correct_answer = word_dict[word]             # Retrieve the correct meaning (in Chinese) of the current English word.
        if user_input == correct_answer:              # Check if the user's input matches the correct meaning and provide feedback.
            print("Correct! ✔️\n")
        else:
            print(f"Wrong. The correct answer is: '{correct_answer}'. ❌\n")

