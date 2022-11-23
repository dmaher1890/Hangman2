#guesses is not going down. 
#duplicate guesses not working.

#from curses.ascii import isalpha
import random 


#chosse a random word from the list
def get_word():
    words = ['word', 'guess', 'another', 'boiler']
    word = random.choice(words)
    return(word)

#split word into a list of letters
def split_word(word):
    letters = []
    for letter in word:
        letters.append(letter)
    return(letters)

#user input to collect the guess
def collect_guess(letters, guessed_letters):
    guessed_letters = []
    loop = True
    while loop == True:
        guess = input("What letter do you want to guess? ")
        if guess in guessed_letters:
            print("Sorry you guessed that letter already")
        elif guess.isalpha():
            guessed_letters.append(guess)
            return(guess)
            break;      
        else:
            print("Sorry that is not a valid guess, try again")
            continue

#check the guess against the word
def check_guess(letters, guess, guessed_letters, guesses_count_left):
    if guess in letters:
        print("Yes that letter is in the word")
        guessed_letters.append(guess)
        return(guessed_letters)
    else:
        print("test guesses left before - 1", guesses_count_left)
        print("Sorry that letter is not in the word")
        guesses_count_left = guesses_count_left - 1
        print("You have", guesses_count_left, "guesses left")
        return(guesses_count_left)

def guesses_count_start(letters): #defines the starting number of guesses the user gets
    guesses_count = 10
    #guesses_count = len(letters)
    return(guesses_count)

def main():
    guessed_letters = []
    word = get_word()
    letters = split_word(word)
    guesses_count_left = int
    guesses_count_left = guesses_count_start(letters)
    print("test main guesses left", guesses_count_left)
    while True:
        if len(letters) == 0: 
            print("You won the word was", word)
            break
        if guesses_count_left == 0:
            print("Sorry you ran out of guesses, the word was", word)
            break
        guess = collect_guess(letters, guessed_letters)
        guessed = check_guess(letters, guess, guessed_letters, guesses_count_left)
        continue

    print("test guess",  guess)
    print("test letters",  letters)
    print("test guesses left", guesses_count_left)


    # ***** can we get this thorugh an API or make it a bigger list automatically
    # ***** Make is 4 letter words, 5 letter words, 6 letter works

main()