import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!= random_number:

        guess=int(input(f"Guess a number between 1 and {x}: "))
        
        if guess <random_number:
            print("Your guess is low, go higher")
        elif guess>random_number:
            print(f"Your guess is high, go lower")
        else:
            print("Congratulations, you have find the number")


guess(10)