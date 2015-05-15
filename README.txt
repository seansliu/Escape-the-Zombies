Escape the Zombie!

Michelle Lee, Sean Liu, Sophie Lucy

Escape the Zombie is a modern take on the classic game of Hangman. Princess 
Peach, our damsel in distress, is about to be eaten by a zombie, and it's up 
to you to save her, by guessing the secret word that stops it!


How to run:
	python Zombiegame.py


Architecture:

Our game consists of the following components:
ZombieGame.py - our main program file
zombie.py - our backend functions
words.txt - textfile containing the 10,000 most commonly used English
words, taken from https://github.com/first20hours/google-10000-english.
images - directory containing images we display during gameplay.


How it works:

We built this game on Python 2.7, with the help of Tkinter and PIL. The game 
is a simple Tk GUI that indexes a dictionary of English words on 
initialization, and interacts with the user to create this unique gameplay 
experience. 

On initialization, ZombieGame indexes the words.txt dictionary and saves our 
pre-created gameplay images in the images folder. Once the user selects a 
difficulty, it picks a random word from the appropriate word length, and 
continues to update the user's guess and game image accordingly. Once the 
game is over, i.e. when the user wins or loses, a final win/lose image is 
written, and the game resets.