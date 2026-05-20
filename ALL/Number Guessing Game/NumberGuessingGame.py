import random
from art import logo

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    
    guessed = False
    
    while attempts > 0 and not guessed:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        if guess == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            guessed = True
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Too low.")
        
        attempts -= 1
    
    if not guessed:
        print(f"You've run out of guesses. The answer was {secret_number}.")

game()