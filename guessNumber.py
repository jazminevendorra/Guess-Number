# Number guessing game where a player will get up to seven chances to guess a mystery
# number in the range of 1 trough 100.
#At the beginning of the game, the program will generate a random number in the range 1 through 100. It will then prompt the player to guess the number. If the user’s guess is:
#
#Higher than the random number => the program will display “Too High …”.
#Lower than the random number => the program will display “Too Low … ”.
#The same as the random number => the program will congratulate the player.


# Import libraries
import random

## Global variables
first = 1
last = 100
rounds = 8

def main():
    #Intro
    print("Guess the Mystery Number ...\n")

    tryAgain = 'y'

    while tryAgain == 'y':
        # Generate random number from 1 to 100
        number = random.randint(1,100)

        ## rounds 
        for round in range(rounds):
            print("Round", round, "of 7")
            print("------------------------------")
            # Get player choice
            guess = getGuess(first,last)
            
            # Compare mystery number agains player guess
            guessWin(number,guess)

        tryAgain =input("Would you like to try again (y/n)? ").lower()
            
        
## Prompts user for guess in range
def getGuess(first,last):
    guess = 1

    guess = int(input("Enter your guess (1-100): "))

    #Validate
    while guess < first or guess > last:
        if guess < first or guess > last:
            print("Error ... Incorrect number. Try again")
        guess = int(input("Enter your guess (1-100): "))
        
        
        
    return guess


## Compare the mystery number against the player's guess.
def guessWin(number,guess):

    if (guess < number):
        print(" ---> ", guess, " is too Low ...\n")
    elif(guess > number):
        print(" ---> ", guess, " is too High ... \n")
    if(guess == number):
        print("\nCongratulations ... You guessed the Mistery Number!\n")
        tryAgain =input("Would you like to try again (y/n)? ").lower()
       
    return 

main()



        
