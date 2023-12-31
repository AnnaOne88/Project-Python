import openpyxl
import random

# STEP 1: Create a function that will read XLS file and create a dictionary of EN-CN pairs.

def read_xlsx(path):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    word_dictionary = {}  # Dictionary to store English-Chinese words

    for row in sheet.iter_rows(min_row=2, values_only=True):
        english_word, chinese_words_str = row   #Changing chinese_word to chinese_words_str, because in our updated vocabulary list, the second column is a string containing more entries separated with commas.

        # Add a check for None before splitting
        if chinese_words_str is not None:
            chinese_words = [word.strip() for word in chinese_words_str.split(',')] # Splitting the chinese_words_str into a LIST of SUBSTRINGS separated with a comma+space
        else:
            chinese_words = [] #this scenario actually happens 5x at the beginning, I dont know why. Add a print() here and you will see...

        word_dictionary[english_word] = chinese_words

    # Filter out entries where Chinese words are empty. I tried this before without filtering and
    # I was getting a lot of None values, even though there were no empty rows in the list before. And I dont know why.
    word_dictionary_filtered = {key: value for key, value in word_dictionary.items() if value}

    return word_dictionary_filtered

path = './vocabulary-list-extended.xlsx' # The path to our XLSX

word_dict = read_xlsx(path)  # Read the XLSX file and create a dictionary

# Print the filtered dictionary to check
'''print("Filtered EN-ZH Dictionary:")
for english_word, chinese_words in word_dict.items():
    print(f"{english_word}: {chinese_words}")

# STEP 3: Let's choose a random key-value pair from the dictionary
random_pair = random.choice(list(word_dict.items()))
random_english_word, random_chinese_words = random_pair
print("\nRandom Word:" f" {random_english_word} - {random_chinese_words} \n")  # This format can be changed'''

word_dict_reduced = word_dict.copy()          #making a copy of the original dict - in case we want to do more rounds of revision. We dont want the original vocabulary list affected...

# STEP 4: Create a list of English words from the keys of the vocabulary dictionary.
words = list(word_dict_reduced.keys())
repetitions = 3    # set how many words we will revise

sum =0 
correctNum = 0
wrongNum = 0
wrong_answers = [] #this list will record which word the user didnt answer correctly

for i in range(repetitions):
    random_english_word = random.choice(words)
    print(f"What is '{random_english_word}' in Chinese?")
    user_input = input("Your answer: ").strip()

    correct_answers = word_dict_reduced[random_english_word]

    words.remove(random_english_word)

    if user_input in correct_answers:
        correctNum += 1
        sum += 1
        print(f"Correct! ✔️ Correct: {correctNum}, Wrong: {wrongNum}, Total revised: {sum}\n")
    else:
        wrongNum += 1
        sum += 1
        print(f"Wrong. The correct answers are: {', '.join(correct_answers)}. ❌, Correct: {correctNum}, Wrong: {wrongNum}, Total revised: {sum}\n")
        wrong_answers.append((random_english_word, correct_answers))

percentage_correct = correctNum/sum*100
print(f"Your success rate is: {percentage_correct:.2f}% correct ({correctNum} out of {sum}) ") #formatting this to 2 decimal places
print('Wrong answers:', wrong_answers)
