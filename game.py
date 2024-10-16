import random
import time


class NumberGuessingGame():
    def __init__(self):
        return None
    
    def startGame(self):
        print('\033[1;34;40mWelcome to the Number Guessing Game!\n')
        time.sleep(1)
        print("\033[0;36;40mI'm thinking of a number between 1 and 100.\n")
        time.sleep(1)
        print('Please select your difficulty level: ')
        time.sleep(0.4)
        print('1. Easy (10 chances)')
        time.sleep(0.4)
        print('2. Medium (5 chances)')
        time.sleep(0.4)
        print('3. Hard (3 chances)')
        time.sleep(0.4)
        while True:
            try:
                self.difficulty = int(input('Enter your choice: '))
                if self.difficulty in range(1,4):
                    break
                else:
                    print('\033[0;36;40mPlease input a valid answear.\n')
            except ValueError:
                print('Please input a number.')
        dictionary = {1: 'Easy',
                      2: 'Medium',
                      3: 'Hard'}
        
        print(f'\nGreat! You have selected the {dictionary[self.difficulty]} level.\n')
        return self.difficulty
    
    def guessedNumber(self):
        self.number = random.randint(1, 101)
        return self.number
    
    def setTries(self):
        self.tries = ''
        if self.difficulty == 1:
            self.tries = 10
        if self.difficulty == 2:
            self.tries = 5
        if self.difficulty == 3:
            self.tries = 3
        print(f'\nYou have {self.tries} to guess the correct number.') 
        return self.tries
    
    def theGame(self):
        self.guesses = 0
        while True:
            print(f'\033[0;36;40mGuesses remaining: {self.tries - self.guesses}')
            self.guess = int(input('Take a guess: '))
            self.guesses += 1
            if self.guess == self.number:
                print(f'\nCongratulations! You guessed the correct number ({self.number}) in {self.guesses} attempt(s)!')
                break
            elif self.guesses == self.tries:
                print(f'\nYou ran out of tries! The number was {self.number}. Better luck next time!')
                break
            else:
                if self.guess < self.number:
                    print(f'\033[1;31;40mIncorrect! The number is greater than {self.guess}')
                elif self.guess > self.number:
                    print(f'\033[1;31;40mIncorrect! The number is less than {self.guess}')
        return None    
    
    
game = NumberGuessingGame()

def main():
    while True:
        game.startGame()
        game.guessedNumber()
        game.setTries()
        game.theGame()
        while True:
            ch = str(input('Do you want to play again? [Y/N]: ')).upper()
            if ch not in 'NY':
                print('Please choose a valid answear.')
            else:
                break
        if ch == 'N':
            print('Bye!')
            break


main()
        








