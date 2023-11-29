import random


def revise_vocabulary(vocabulary):
    """
    Function to revise vocabulary in a foreign language.

    Parameters:
    - vocabulary: a dictionary where keys are words in English and values are their meanings in Chinese.
    """
    # Create a list of English words from the keys of the vocabulary dictionary.
    words = list(vocabulary.keys())

    # Shuffle the order of English words for a varied quiz experience.
    random.shuffle(words)

    # Iterate through each English word in the shuffled list.
    for word in words:
        # Print a prompt asking for the meaning of the current English word.
        print(f"What is '{word}' in Chinese?")

        # Take user input for the meaning of the current English word.
        user_input = input("Your answer: ").strip()

        # Retrieve the correct meaning (in Chinese) of the current English word.
        correct_answer = vocabulary[word]

        # Check if the user's input matches the correct meaning and provide feedback.
        if user_input == correct_answer:
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
