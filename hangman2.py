
#need to test for a valid entry

import random 

words = ['word', 'guess', 'another', 'boiler']
word = random.choice(words)
guessed_letters = []
masked_letters = []

def show_masked_letters(word):
    display = []
    letters = []
    for l in word:
        letters.append('#')
    print("Test letters left", letters)
    return masked_letters
    

def show_letters_found(masked_letters, guessed_letters):
    pass
    # take word at it to a dictinary, if the letter is in the word replace that letter in masked_letter in the same location

letters = []
for letter in word:
    letters.append(letter)

guesses_count = 10

while True:
    if len(letters) == 0: 
        print("You won the word was", word)
        break
    elif guesses_count == 0:
        print("Sorry you ran out of guesses, the word was", word)
        break
    else: guess = input("What letter do you want to guess? ")
    if guess in guessed_letters:
        print("Sorry you guessed that letter already")
    else:
        if guess in letters:
            print("Yes that letter is in the word")
            guessed_letters.append(guess)
            letters.remove(guess)
            show_letters_found(masked_letters, guessed_letters)
            print("Current correct letters are: ", guessed_letters)
            print("Letters left in the word ", (show_masked_letters(word)))
        else:
            print("Sorry that letter is not in the word")
            guesses_count = guesses_count - 1
            guessed_letters.append(guess)
            masked_letters = show_masked_letters(word) 
            print("You have", guesses_count, "incorrect guesses left")
            print("Letters left in the word ", masked_letters)
        #print("test letters",  letters)
        #print("guessed letters", guessed_letters)
        continue
