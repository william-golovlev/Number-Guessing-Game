#This is a guessing the number game, I wanted to test out Python.
import random, sys

print('Welcome to my first Python program. What\'s your name?')
name = input()

print('Howdy, ' + name + '. I am thinking of a number between 1 and 20.')
secretNum = random.randint(1,20)

for guesses in range(1, 7):
    try:
        guess = int(input('Take a guess:\n'))
    except:
        print('\nError: put an integer.')

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break #If int is guessed

if guess == secretNum:
    print('Good job, ' + name + '! You guessed the number ' + str(secretNum) + ' in ' + str(guesses) + ' guesses.')
else:
    print('Nope, the number I was thinking of was ' + str(secretNum) + ', you lose.')

sys.exit()

