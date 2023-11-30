#This is a template. It is using a DICTIONARY defined below. There are many other ways to revise, but lets start with something!

import random


def revise_vocabulary(vocabulary):
    """
    Function to revise vocabulary in a foreign language.
    This function has one parameter:vocabulary. This param is a dictionary where keys are words in English and values are their meanings in Chinese.
    """
    
    words = list(vocabulary.keys())    # Create a list of English words from the keys of the vocabulary dictionary.

    random.shuffle(words)    # Shuffle the order of English words for a varied quiz experience.

    # Iterate through each English word in the shuffled list.
    for word in words:
        print(f"What is '{word}' in Chinese?")        # Print a prompt asking for the meaning of the current English word. The 'f' before the string indicates the use of an f-string in Python. F-strings, or formatted string literals, were introduced in Python 3.6. They provide a concise and convenient way to embed expressions inside string literals, using curly braces {} to enclose the expressions.
        user_input = input("Your answer: ").strip()   # Take user input for the meaning of the current English word. --- .strip() removes white spaces from the input.
        correct_answer = vocabulary[word]             # Retrieve the correct meaning (in Chinese) of the current English word.
        if user_input == correct_answer:              # Check if the user's input matches the correct meaning and provide feedback.
            print("Correct! ✔️\n")
        else:
            print(f"Wrong. The correct answer is: '{correct_answer}'. ❌\n")


if __name__ == "__main__":
    '''In Python, the special variable __name__ is used to determine whether a Python script is being run as the main program or 
if it is being imported as a module into another script. The expression __name__ == "__main__" is a common idiom that checks 
if the script is being run directly. Here's how it works: When a Python script is executed, the interpreter sets the __name__ variable. 
If the script is the main program being run, __name__ is set to "__main__". If the script is being imported as a module, __name__ is set to 
the name of the module. The statement if __name__ == "__main__": checks whether the script is the main program (not imported as a module). If it is, the code block following this statement will be executed.'''

    # Example vocabulary with English-Chinese word pairs (replace this with your own).
    my_vocabulary = {
        "hello": "你好",
        "cat": "猫",
        "tree": "树",
        # Add more words and meanings as needed
    }

    # Print a welcome message and start the vocabulary revision quiz.
    print("Welcome to the Vocabulary Revision Program!\n")
    revise_vocabulary(my_vocabulary)
