#These exercises cover a range of basic programming concepts in Python

#Exercise 1: Hello, World!
# Write a Python program that prints "Hello, World!"

print("Hello, World!")


#Exercise 2: Variables and Input
#Create a program that asks the user for their name, then prints a greeting.
name = input("What is your name? ")
print(f"Hello, {name}!")


#Exercise 3: Basic Calculator
#Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")


#Exercise 4: Even or Odd
#Write a program that checks if a given number is even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#Exercise 5: List Manipulation
#Create a program that defines a list of numbers and prints the square of each number.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")


#Exercise 6: String Manipulation
#Write a program that reverses a given string.\

original_string = input("Enter a string: ")
reversed_string = original_string[::-1]
print(f"Reversed string: {reversed_string}")


#Exercise 7: Guess the Number
#Create a simple number guessing game. Generate a random number between 1 and 100 and let the user guess the number.
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (between 1 and 100): "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
