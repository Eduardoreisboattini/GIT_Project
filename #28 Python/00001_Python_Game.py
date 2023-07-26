### 
### This code is a simple example of how to write a game of words challenge in Python. 
# It uses a list of words to randomly select a word for the player to guess. 
# The player has 5 lives, and they lose a life for each incorrect guess. 
# The player wins the game if they are able to guess all the letters in the word before they run out of lives.
### To run this code, you will need to save it as a Python file and then run it from the command line. 
# For example, if you saved the code as word_challenge.py, you could run it by typing the following command into a command prompt:
# python word_challenge.py
# I hope you will enjoy this game.
### 
### 

import random

def get_random_word():
  """Returns a random word from a list of words."""
  with open("words.txt", "r") as f:
    words = f.readlines()
  word = random.choice(words).strip()
  return word

def is_valid_guess(guess, word):
  """Returns True if the guess is a valid letter in the word, False otherwise."""
  if guess not in word:
    return False
  else:
    return True

def play_game():
  """Plays a game of words challenge."""
  word = get_random_word()
  guessed_letters = []
  lives = 5
  while lives > 0:
    guess = input("Guess a letter: ")
    if is_valid_guess(guess, word):
      guessed_letters.append(guess)
      if all(letter in guessed_letters for letter in word):
        print("You win!")
        break
    else:
      lives -= 1
      print("That letter is not in the word. You have {} lives left.".format(lives))
  if lives == 0:
    print("You lose! The word was {}".format(word))

if _name_ == "_main_":
  play_game()