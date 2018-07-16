from random import *
n = randint(1, 101)
guess = 0
guesses = 0
while guess != n:
    guess = input("Guess my number:")
    if(guess == n):
        print("You got it!")
        if(guesses == 0):
            print("You got it on the first try!")
        if(guesses == 1):
            print("You only got it wrong once!")
        if(guesses >= 2):
            print("You got it wrong "+str(guesses)+" times.")
    elif(guess > n):
        print("Too High!")
    else:
        print("Too Low!")
    guesses+=1
    