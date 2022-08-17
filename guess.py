# Get input ... could also just be print, but input allows to press enter to start
# Can use conditionals to define input
input("Think of a number between 1 and 50. Press ENTER to start.")

# Define guesses
num_guesses = input("Hor many guesses does the computer get? ")
num_guesses = int(num_guesses)

# Define range of guess (min, max)
low = 1
high = 50

# 6 parts to a for loop: for, variable, in, collection, colon, body
for guess_num in range(num_guesses): # range returns a collention ("sequence"), not an int; guess_num (variable) holds whatever gets returned from range()

    # Guess integer between min, max
    guess = int((low + high) / 2)
    print("Is", guess, "your number? Please answer with higher, lower, or correct.")

    # Obtain and report answer
    answer = input("Answer: ").lower()

# # Tell if correct or incorrect
# if answer == "higher":
#     low = guess + 1
# elif answer == "lower":
#     high = guess - 1
# elif answer == "correct":
#     print("Computer correctly guessed:", guess) # input/output don't always have new line, may want to add \n
# else:
#     print("Invalid input! Try again.")
