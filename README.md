# Word Guessing Game (Hangman Style)

A fun **word-guessing game** built in **Python**, where the player guesses letters of a hidden word before running out of attempts. Choose your difficulty level and test your guessing skills!  

---

## Features

- Randomly selects a word from a predefined **word bank**.  
- Three difficulty levels:
  - **Easy** → 12 attempts  
  - **Medium** → 10 attempts  
  - **Hard** → 6 attempts  
- Displays the current guessed letters with underscores for remaining letters.  
- Tracks remaining attempts and gives feedback on each guess.  
- Option to **play again** after each round.  
- Beginner-friendly, console-based game.

---

## How It Works

1. Player is asked if they are ready to play.  
2. Player selects a difficulty level (easy, medium, hard) to set attempts.  
3. The game randomly selects a word from the word bank.  
4. Player guesses letters one at a time:  
   - Correct guesses reveal the letters in the word.  
   - Incorrect guesses reduce the remaining attempts.  
5. The game continues until:  
   - The player correctly guesses the entire word (**win**).  
   - The player runs out of attempts (**lose**).  
6. At the end of the game, the player can choose to play again.

---

## Inputs

- **Ready to play?** – `True` or `False`  
- **Difficulty level:** `easy`, `medium`, `hard`  
- **Letter guesses:** Single letters only  
- **Play again?** – `True` or `False`  

---

## Example Gameplay

```text
Are you ready to play (True/false): True
Enter the difficulty level(Easy -12/Medium -10/Hard -6) : Medium

let begin the game .....

Current word: _ _ _ _ _ _ _
Guess a letter: e
Great Guess!
Current word: _ e _ _ _ _ _
Guess a letter: a
Try again! Attempts left: 9
...
Congratulation!! You guessed the word: rainbow
Do you want to play again: False
See you soon...
