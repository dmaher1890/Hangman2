#need to test for a valid entry
#skill levels

import random #To randomly choose a word

#Function to mask the letters on the word
def show_masked_letters(word):
    display = []
    masked_letters = []
    for l in word:
        masked_letters.append('#')
    return masked_letters 

#Function to unmask only the foun letters
def show_letters_found(word, masked_letters, guessed_letters):
    letters = []
    for l in word:
        letters.append(l)
    for i in guessed_letters: 
        if i in letters:
            location = letters.index(i)
            masked_letters[location] = i
    print("Missing letters left in the word ", masked_letters)

#words to choose from
words = ['word', 'guess', 'another', 'boiler']

#randomly choose word
word = random.choice(words)

#list to store the guessed letters right or wrong
guessed_letters = []

#calling to mask the letters in the found word
masked_letters = show_masked_letters(word) 

#number of guesses the user gets
guesses_count = 6

#split the word into its letters and put them in a list
letters = []
for letter in word:
    letters.append(letter)

#flow of the application
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
            show_letters_found(word, masked_letters, guessed_letters)
            print("Current correct letters are: ", guessed_letters)
        else:
            print("Sorry that letter is not in the word")
            guesses_count = guesses_count - 1
            guessed_letters.append(guess)
            show_letters_found(word, masked_letters, guessed_letters)
            print("You have", guesses_count, "incorrect guesses left")

        continue