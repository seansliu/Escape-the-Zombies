# Zombie Game GUI
#
# Michelle Lee, Sean Liu, Sophie Lucy

from zombie import *
import Tkinter as Tk
from PIL import Image, ImageTk

test = 'zombie'

class ZombieGame:
	"""Escape the Zombie Game"""

	def __init__(self):
		"""defines the GUI window"""
		self.main_window = Tk.Tk()
		self.main_window.title('Escape the Zombies!')

		# create the window frames
		self.top_frame = Tk.Frame()
		self.difficulty_frame = Tk.Frame()
		self.mid_frame = Tk.Frame()
		self.word_frame = Tk.Frame()
		self.guess_frame = Tk.Frame()
		self.play_frame = Tk.Frame()
		self.quit_frame = Tk.Frame()
		self.stats_frame = Tk.Frame()

		# initialize images
		self.images = [	ImageTk.PhotoImage(Image.open('images/zombies.jpg')),
						ImageTk.PhotoImage(Image.open('images/zombies2.jpg'))
						]

		# initizlize data structures
		self.word_bank = {}
		self.word = ''
		self.guess = []
		self.mistakes = 0

		# directions frame
		self.direction = Tk.StringVar(value='Select a difficulty to begin.')
		self.dir_label = Tk.Label(self.top_frame, width=100, bg='cyan', \
			textvariable=self.direction)
		self.dir_label.pack(side='left')

		# difficulty buttons
		self.easy_butt = Tk.Button(self.difficulty_frame, text='Easy')
		self.easy_butt.pack(side='left')
		self.medium_butt = Tk.Button(self.difficulty_frame, text='Medium')
		self.medium_butt.pack(side='left')
		self.hard_butt = Tk.Button(self.difficulty_frame, text='Hard')
		self.hard_butt.pack(side='left')

		# gameplay image
		self.image_label = Tk.Label(self.mid_frame, image=self.images[0])
		self.image_label.pack(side='top', fill='both', expand='yes')

		# word display frame
		self.display = Tk.StringVar()
		self.word_label = Tk.Label(self.word_frame, width=100, bg='yellow', \
			textvariable=self.display)
		self.word_label.pack(side='left')

		# input frame
		self.entry = Tk.Entry(self.guess_frame, width=2)
		self.guess_butt = Tk.Button(self.guess_frame, text='Guess')
		self.entry.pack(side='left')
		self.guess_butt.pack(side='left')


		# Play and Quit frames.
		self.replay_butt = Tk.Button(self.play_frame, text='Replay')
		self.quit_butt = Tk.Button(self.quit_frame, text='Quit', 
			command=self.quit_now)
		self.replay_butt.pack(side='left')
		self.quit_butt.pack(side='right')
		self.reset()

		# Stat tracking frame.
		self.stats = Tk.StringVar(value = 'Avg. number of guesses to win: ')
		self.stats_label = Tk.Label(self.stats_frame, \
								   textvariable = self.stats)
		self.stats_label.pack(side = 'left')

		# Pack frames.
		self.top_frame.pack()
		self.difficulty_frame.pack()
		self.mid_frame.pack()
		self.word_frame.pack()
		self.guess_frame.pack()
		self.play_frame.pack(side = 'left')
		self.quit_frame.pack(side = 'right')
		self.stats_frame.pack()

		# Variables needed in play function.
		self.comp = Tk.StringVar()
		self.tries = Tk.IntVar()
		self.wintries = Tk.IntVar(value = 0)
		self.wins = Tk.IntVar(value = 0)
		
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
		if mode == 0:
			print 0
		elif mode == 1:
			print 1
		else:
			print 2

		self.image_label.configure(image=self.images[1])
		self.replay_butt.configure(command=self.reset)
		self.easy_butt.configure(command=self.chill)
		self.medium_butt.configure(command=self.chill)
		self.hard_butt.configure(command=self.chill)
		self.guess_butt.configure(command=self.check_letter)
		self.word = test
		self.mistakes = 0
		self.guess = len(self.word) * ['_']
		display = ' '.join(self.guess)
		self.display.set(display)
		self.direction.set('Please guess a letter below.')


	def reset(self):
		"""resets the game"""
		self.image_label.configure(image=self.images[0])
		self.replay_butt.configure(command=self.chill)
		self.easy_butt.configure(command=self.start_easy)
		self.medium_butt.configure(command=self.start_medium)
		self.hard_butt.configure(command=self.start_hard)
		self.guess_butt.configure(command=self.chill)
		self.word = ''
		self.guess = ''
		self.display.set('')
		self.direction.set('Select a difficulty to begin.')
		

	def check_letter(self):
		"""checks input letter with word"""
		letter = self.entry.get()
		print letter
		if len(letter) != 1:
			return

		if (letter in self.word) and not (letter in self.guess):
			for i in range(len(self.word)):
				if self.word[i] == letter:
					self.guess[i] = letter
			display = ' '.join(self.guess)
			self.display.set(display)

			if self.word == ''.join(self.guess):
				print 'win'

		else:
			self.mistakes += 1
			# new badder image

			if self.mistakes == 6:
				print 'lose'


	def chill(self):
		"""do nothing"""
		return
		

	def quit_now(self):
		'''destroys the GUI'''
		self.main_window.destroy()


z = ZombieGame()

