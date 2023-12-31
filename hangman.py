words = ('sample','amazing','able', 'unit','packet','national','mark','heart','head','content','term','dress','skip','pollution','overview','chaos','live','silver','gold','student')

import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word    

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        print('You have',lives,'used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current Word:' , ' '.join(word_list))

        user_letter = input('Guess the letter').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print("The letter is not a word..! ")    
    
        elif user_letter in used_letters:
            print("Your already used the letter..!")  
    
        else:
            print("Invalid charcter, please try again..! ")    

    if lives == 0:
        print("You lost..!") 

    else:
        print(f"The word is {word}")           
            


hangman()

