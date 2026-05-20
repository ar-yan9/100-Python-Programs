import random

HANGMAN_PICS = [
    """
     -----
     |   |
         |
         |
         |
         |
    ==========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    ==========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    ==========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    ==========""",
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    ==========""",
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    ==========""",
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========="""]

words = ["python", "hangman", "programming", "keyboard",
         "developer", "variable", "function", "iteration"]

def play():
    word = random.choice(words)
    guessed = set()
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0:
        display = [c if c in guessed else "_" for c in word]
        print(HANGMAN_PICS[6 - tries])
        print(" ".join(display))
        print(f"Tries left: {tries} | Guessed: {sorted(guessed)}")

        if "_" not in display:
            print(f"\n🎉 You won! The word was '{word}'")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
        elif guess in guessed:
            print("Already guessed that!")
        elif guess in word:
            guessed.add(guess)
            print("✅ Correct!")
        else:
            guessed.add(guess)
            tries -= 1
            print("❌ Wrong!")

    print(HANGMAN_PICS[6])
    print(f"\n💀 Game over! The word was '{word}'")

play()