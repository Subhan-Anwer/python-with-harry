'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file 'Hi-score.txt' which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score.
'''

import random

def game():
    secret_number = random.randint(1, 10)
    attempts = 0
    score = 10

    print("\n🎯 Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10... Can you guess it?")

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1
            score = score - 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You got it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")
            
            
    

    return score


your_score = game()
print(f"your score is {your_score}")


# High score logic

# Read existing high score
with open("Hi-score.txt", "r") as f:
    try:
        high_score = int(f.read().strip())
    except ValueError:
        high_score = 1

# Compare and update if new score is better
if your_score > high_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(your_score))
    print("🏆 New High Score!")

