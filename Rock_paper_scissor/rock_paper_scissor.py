import random

def play():
    while True:
        user = input("R for rock, P for paper, and S for scissors: ").lower()
        if user not in ["r", "p", "s"]:
            print("This is not defined, try again.")
        else:
            break
    
    computer = random.choice(["r", "p", "s"])
    print(f"Computer chose {computer}")

    if computer == user:
        return "It's a tie!"
    elif user_win(user, computer):
        return "You have won!"
    else:
        return "You have lost."

def user_win(player, computer):
    return (player == "r" and computer == "s") or \
           (player == "s" and computer == "p") or \
           (player == "p" and computer == "r")

print(play())
