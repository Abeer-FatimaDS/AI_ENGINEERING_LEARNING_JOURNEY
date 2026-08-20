import random

comp = random.randint(1,100)
user = 0
Try = 0
while user != comp:
    user = int(input("Enter your guess Number: " ))
    if (comp < user):
        print("Guess some lower number")
    else:
        print("Guess some higher number")
    Try = Try + 1
print(f"You won. You guesses it right in {Try} tries")
