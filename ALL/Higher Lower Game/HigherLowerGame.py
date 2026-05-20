 
from art import logo, vs
from game_data import data
import random

def get_random_account():
    return random.choice(data)

def get_follower_count(account):
    return account["follower_count"]

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

        guess = input("Who has more followers? Type 'a' or 'b': ").lower()

        a_followers = get_follower_count(account_a)
        b_followers = get_follower_count(account_b)
        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")

game()