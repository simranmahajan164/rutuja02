# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and user interactions.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game by creating a word list and implementing a mechanism to randomly select a hidden word for each game.

#### Requirements
Completed program should:

- Store a list of at least 10 words for the game
- Randomly select a word at the start of each game
- Initialize variables to track the game state (guessed letters, remaining attempts, etc.)

### 🛠️ Guess Handling and Progress Display

#### Description
Implement the core guessing functionality that accepts player input and displays the current progress.

#### Requirements
Completed program should:

- Accept single letter guesses from the player
- Show current progress with revealed letters and blanks (e.g., `_ _ b a n a n a`)
- Track and display incorrect guesses remaining
- Prevent duplicate guesses and handle invalid inputs

### 🛠️ Win/Lose Conditions and Game Flow

#### Description
Implement game ending conditions and create the main game loop.

#### Requirements
Completed program should:

- End the game when the word is guessed correctly or attempts are exhausted
- Display appropriate win/lose messages
- Allow the player to play multiple games
- Keep track of wins and losses across multiple games
