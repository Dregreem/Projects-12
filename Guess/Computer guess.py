import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback.lower() != "c" and low <= high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too High (H/h), too Low (L/l), or Correct (C/c)? ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("Wrong input")
    
    print(f"Your number is: {guess}")

computer_guess(10)
