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
words.txt - dictionary containing the 10,000 most commonly used English
words, taken from https://github.com/first20hours/google-10000-english.


How it works:

We built this game on Python 2.7, with the help of the Tkinter and PIL. The 
game is a simple Tk GUI that indexes a dictionary of English words on 
initialization, and interacts with the user to create this unique gameplay 
experience. 

On initialization, ZombieGame indexes the words.txt dictionary and saves our 
pre-created gameplay images in the images folder. Once the user selects a 
difficulty, it picks a random word from the appropriate word length, and 
continues to update the user's guess and game image accordingly. Once the game 
is over, i.e. when the user wins or loses, a final win/lose image is written, 
and the game resets.

<a package you liked/disliked>

We encountered several problems while working with our code. There are obvious problems that occur when working on a specific part of the project within a group: each person may have different coding styles, and it it difficult, though certainly not impossible to try to make each individual part work seamlessly into the whole. We overcame this problem by making sure we worked together as much as possible so we would all be aware of the foundational structure of our program.

One of the first programming problems we encountered was working with .jpeg for our images. Even after downloading the appropriate software, some of our members were unable to view the images upon running the program, so we had to switch to the less common .ppm files. 

Another problem we ran into was deciding on an initial structure for our GUI. We played around with the idea of having one window that would reset on top of each other for the three main parts of the game (game start, game play, game stats). In the end, we decided to combine all three frames into one larger window for convenience. 

In addition, it was at times difficult to acquaint ourselves with the way TKinter works, in terms of navigating between variables and methods that would work simply in Python, but would not have a parallel method in Tkinter. For example, when creating the incorrect letters bank, we decided to create a string variable over a TkStringVar because it was easier to add to a regular string and reset the label each time, over trying to find an attribute to adding to a TkStringVar. 

<something that worked out nicely>: being able to hit enter instead of always clicking the guess button. Played around with the idea of silently listening for keyboard input when guessing letters during gameplay, but…

<something that didn’t work at all> ?

<was python the right tool for the project?> not necessarily. could have made a web app using html, css, javascript; could have added many more features such as multiple pages, music, etc.