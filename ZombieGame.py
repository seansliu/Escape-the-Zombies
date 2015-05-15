# Zombie Game GUI
#
# Michelle Lee, Sean Liu, Sophie Lucy

from zombie import *
import Tkinter as Tk
from PIL import Image, ImageTk

class ZombieGame:
	"""Escape the Zombie Game"""

	def __init__(self):
		"""define the GUI window"""
		self.main_window = Tk.Tk()
		self.main_window.title('Escape the Zombies!')

		# create the window frames
		self.top_frame = Tk.Frame()
		self.difficulty_frame = Tk.Frame()
		self.mid_frame = Tk.Frame()
		self.word_frame = Tk.Frame()
		self.guess_frame = Tk.Frame()
		self.wrong_frame = Tk.Frame()
		self.play_frame = Tk.Frame()
		self.quit_frame = Tk.Frame()
		self.stats_frame = Tk.Frame()

		# initialize images
		self.images = []
		for i in range(7):
			filename = 'images/zombies' + str(i) + '.ppm' 
			self.images.append(ImageTk.PhotoImage(Image.open(filename)))
		self.game_img = ImageTk.PhotoImage(Image.open('images/zombies.ppm'))
		self.win_img = ImageTk.PhotoImage(Image.open('images/win.ppm'))
		self.lose_img = ImageTk.PhotoImage(Image.open('images/lose.ppm'))

		# initizlize data structures
		self.wordbank = index_dict('words.txt')
		self.word = ''
		self.guess = []
		self.guesses = []
		self.wrongbox = ''
		self.mistakes = 0
		self.badguess = 0
		self.badguess_total = 0
		self.loss = 0
		self.wins = 0
				
		# directions frame
		self.direction = Tk.StringVar(value='Select a difficulty to begin.')
		self.dir_label = Tk.Label(self.top_frame, width=60, bg='cyan', \
			textvariable=self.direction, font=("Helvetica", 20))
		self.dir_label.pack(side='left')

		# difficulty buttons
		self.easy_butt = Tk.Button(self.difficulty_frame, text='Easy', \
			font=("Helvetica", 20))
		self.easy_butt.pack(side='left')
		self.medium_butt = Tk.Button(self.difficulty_frame, text='Medium', \
			font=("Helvetica", 20))
		self.medium_butt.pack(side='left')
		self.hard_butt = Tk.Button(self.difficulty_frame, text='Hard', \
			font=("Helvetica", 20))
		self.hard_butt.pack(side='left')

		# gameplay image
		self.image_label = Tk.Label(self.mid_frame, image=self.game_img)
		self.image_label.pack(side='top', fill='both', expand='yes')

		# word display frame
		self.display = Tk.StringVar()
		self.word_label = Tk.Label(self.word_frame, width=60, bg='yellow', \
			textvariable=self.display, font=("Helvetica", 20))
		self.word_label.pack(side='left')

		# wrong letters bank
		self.wrong = Tk.StringVar()
		self.wrong_label1 = Tk.Label(self.wrong_frame, width=60, bg='red', \
			text='Incorrectly guessed letters:', font=("Helvetica", 20))
		self.wrong_label2 = Tk.Label(self.wrong_frame, width=60, bg='red', \
			textvariable=self.wrong, font=("Helvetica", 20))
		self.wrong_label1.pack()
		self.wrong_label2.pack()

		# input frame
		self.entry = Tk.Entry(self.guess_frame, width=2, \
			font=("Helvetica", 20))
		self.guess_butt = Tk.Button(self.guess_frame, text='Guess', \
			font=("Helvetica", 20))
		self.entry.pack(side='left')
		self.guess_butt.pack(side='left')

		# Play and Quit frames.
		self.replay_butt = Tk.Button(self.play_frame, text='Replay', \
			font=("Helvetica", 20))
		self.quit_butt = Tk.Button(self.quit_frame, text='Quit', 
			command=self.quit_now, font=("Helvetica", 20))
		self.replay_butt.pack(side='left')
		self.quit_butt.pack(side='right')
		self.reset()

		# stat tracking frame.
		self.stats = Tk.StringVar()
		self.stats_label = Tk.Label(self.stats_frame, \
			textvariable=self.stats, font=("Helvetica", 20))
		self.stats_label.pack(side='left')

		# pack frames.
		self.top_frame.pack()
		self.difficulty_frame.pack()
		self.mid_frame.pack()
		self.word_frame.pack()
		self.guess_frame.pack()
		self.stats_frame.pack()
		self.wrong_frame.pack()
		self.play_frame.pack(side='left')
		self.quit_frame.pack(side='right')

		# Variables needed in play function.
		self.comp = Tk.StringVar()

		Tk.mainloop()


	def start_easy(self):
		"""start game in easy mode"""
		self.start(0)


	def start_medium(self):
		"""start game in easy mode"""
		self.start(1)


	def start_hard(self):
		"""start game in easy mode"""
		self.start(2)


	def start(self, mode):
		"""initialize the game"""
		# sleep unrelated buttons
		self.easy_butt.configure(command=self.chill)
		self.medium_butt.configure(command=self.chill)
		self.hard_butt.configure(command=self.chill)

		self.image_label.configure(image=self.images[0])
		self.guess_butt.configure(command=self.check_letter)
		self.replay_butt.configure(command=self.reset)
		self.direction.set('Save Peach! Please guess a letter below.')
		self.main_window.bind('<Return>', self.check_letter)

		self.badguess = 0
		self.mistakes = 0
		self.word = generate_word(self.wordbank, mode)
		self.guess = len(self.word) * ['_']
		for i in range(len(self.word)):
			if not self.word[i].isalpha():
				self.guess[i] = self.word[i]
		display = ' '.join(self.guess)
		self.display.set(display)


	def reset(self):
		"""resets the game"""
		# sleep unrelated buttons
		self.replay_butt.configure(command=self.chill)
		self.guess_butt.configure(command=self.chill)

		self.image_label.configure(image=self.game_img)
		self.easy_butt.configure(command=self.start_easy)
		self.medium_butt.configure(command=self.start_medium)
		self.hard_butt.configure(command=self.start_hard)
		self.guesses = []
		self.wrongbox.set = ''
		self.wrong.set(self.wrongbox)
		self.display.set('')
		self.direction.set('Select a difficulty to begin.')
		

	def check_letter(self, *args):
		"""checks input letter with word"""
		letter = self.entry.get()
		if len(letter) != 1 or not letter.isalpha():
			self.direction.set('Invalid input. Please enter an letter ONLY.')
			return
		letter = letter.lower()

		# correct guess
		if (letter in self.word.lower()) and not (letter in self.guesses):
			self.guesses.append(letter)
			for i in range(len(self.word)):
				if self.word[i].lower() == letter:
					self.guess[i] = self.word[i]
			display = ' '.join(self.guess)
			self.display.set(display)
			self.direction.set('Nice guess. Keep it up!')

			if self.word == ''.join(self.guess):
				self.win()
				self.main_window.unbind('<Return>')
			return

		# wrong guess
		self.mistakes += 1

		self.wrongbox = self.wrongbox + ' ' + letter

		self.wrong.set(self.wrongbox)

		if self.mistakes >= 7:
			self.lose()
			self.main_window.unbind('<Return>')
		else:
			self.image_label.configure(image=self.images[self.mistakes])
			self.direction.set('Oops! Wrong letter. Try harder!')
			self.badguess += 1


	def quit_now(self):
		"""quits the game by closing the GUI window"""
		self.main_window.destroy()


	def chill(self):
		"""do nothing"""
		return
	

	def win(self):
		"""win state"""
		self.image_label.configure(image=self.win_img)
		msg = 'Congratulations, you saved Peach! Hit Replay to play again.'
		self.direction.set(msg)
		self.guess_butt.configure(command=self.chill)
		self.update_stats(win=True)


	def lose(self):
		"""loss state"""
		self.image_label.configure(image=self.lose_img)
		msg = 'Aw, you failed! Your word: %s. Hit Replay to play again.' \
		%self.word
		self.direction.set(msg)
		self.guess_butt.configure(command=self.chill)
		self.update_stats(win=False)


	def update_stats(self, win):
		"""update and displat stats"""
		self.badguess_total += self.badguess
		if win:
			self.win += 1
		else:
			self.loss += 1
		stats_msg = 'Wins: %d, Losses:%d, Avg. bad guesses: %.2f' \
		%(self.wins, self.loss, \
			float(self.badguess_total)/(self.wins+self.loss))
		self.stats.set(stats_msg)


z = ZombieGame()
