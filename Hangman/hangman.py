import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Ensure the word is uppercase

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Separate all the letters as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    live=10

    while len(word_letters) > 0 and live>0 :
        print("You have used these letters:", ' '.join(used_letters))
        print(f"You have {live} lives")

        # Current word:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word:", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                live=live-1
                print("Sorry this is not the letter")
        
        elif user_letter in used_letters:
            print("You have already guessed this letter")

        else:
            print("Invalid character, please guess a letter")
            

    if live==0:
        print("Sorry you have died")
        print(f" the word {word}!!")

    else:
        print(f"Congratulations! You guessed the word {word}!!")

hangman()
