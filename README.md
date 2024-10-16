# Number Guessing Game

This is a simple command-line game where the player attempts to guess a randomly generated number between 1 and 100. The game allows the player to choose a difficulty level, which determines how many attempts they get to guess the correct number. After each guess, the game will tell the player whether the guessed number is too high or too low. The player can choose to play again or exit after each game session.

## Features

- Three difficulty levels:
  - **Easy**: 10 attempts
  - **Medium**: 5 attempts
  - **Hard**: 3 attempts
- Feedback on each guess (whether it's higher or lower than the correct number)
- Option to play again after the game finishes

## How to Play

1. Run the script.
2. Select a difficulty level by entering a number (1, 2, or 3):
   - 1 for Easy (10 attempts)
   - 2 for Medium (5 attempts)
   - 3 for Hard (3 attempts)
3. The game will generate a random number between 1 and 100.
4. Enter your guess.
5. The game will tell you if the number is higher or lower than your guess.
6. Continue guessing until you either guess the correct number or run out of attempts.
7. After the game, you can choose to play again by entering 'Y' or 'N' when prompted.

## Example Gameplay

Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Please select your difficulty level:

Easy (10 chances)
Medium (5 chances)
Hard (3 chances)
Enter your choice: 1 Great! You have selected the Easy level.

You have 10 chances to guess the correct number.

Guesses remaining: 10 Take a guess: 50 Incorrect! The number is less than 50

Guesses remaining: 9 Take a guess: 25 Incorrect! The number is greater than 25

...

Congratulations! You guessed the correct number (37) in 5 attempts! Do you want to play again? [Y/N]: N Bye!


## Requirements

- Python 3.x
- No additional libraries are required.

## How to Run

To play the game, simply run the script in a terminal or command line:

```bash
python number_guessing_game.py
```

Code Structure
NumberGuessingGame class: Contains all the game logic.
startGame(): Handles the welcome message and difficulty selection.
guessedNumber(): Generates the random number to guess.
setTries(): Sets the number of tries based on the chosen difficulty.
theGame(): The main game loop where the player makes guesses.
main() function: Runs the game, handles restarting the game, and exits when the player chooses not to play again.

Project URL: **https://roadmap.sh/projects/number-guessing-game**
