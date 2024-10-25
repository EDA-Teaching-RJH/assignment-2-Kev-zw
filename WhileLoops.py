### Part Two -- your code goes here. 
import random 
number_to_guess = random.randint(1, 100)
guess = None 
print("Would you like to play a game?")
print("I'm thinking of a number between 1 and 100.")

while guess != number_to_guess:
    try : guess = int(input("Enter Your Guess: "))
    except ValueError:
        print("Please enter a valid number.")
    if guess < number_to_guess: 
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else: print ("Congratulations! You guessed the correct number!")
    