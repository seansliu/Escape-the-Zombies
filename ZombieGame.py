# Zombie Game GUI
#
# Michelle Lee, Sean Liu, Sophie Lucy


from zombie import *
import Tkinter as Tk
from PIL import Image, ImageTk

class ZombieGame:
	def __init__(self):
		"""defines the GUI window"""
		self.main_window = Tk.Tk()
		self.main_window.title('Escape the Zombies!')

		# create the window frames
		self.top_frame = Tk.Frame()
		self.difficulty_frame = Tk.Frame()
		self.mid_frame = Tk.Frame()
		self.word_frame = Tk.Frame()
		self.play_frame = Tk.Frame()
		self.quit_frame = Tk.Frame()
		self.stats_frame = Tk.Frame()

		# directions frame
		self.direction = Tk.StringVar(value='Select a difficulty to begin.')
		self.dir_label = Tk.Label(self.top_frame, width=100, bg='cyan', \
			textvariable=self.direction)
		self.dir_label.pack(side='left')

		# difficulty buttons
		self.easy_butt = Tk.Button(self.difficulty_frame, text='Easy', 
			command=self.start_easy)
		self.easy_butt.pack(side='left')
		self.medium_butt = Tk.Button(self.difficulty_frame, text='Medium', 
			command=self.start_medium)
		self.medium_butt.pack(side='left')
		self.hard_butt = Tk.Button(self.difficulty_frame, text='Hard', 
			command=self.start_hard)
		self.hard_butt.pack(side='left')

		# gameplay image
		self.image = ImageTk.PhotoImage(Image.open('images/zombies.jpg'))
		self.image_label = Tk.Label(self.mid_frame, image=self.image)
		self.image_label.pack(side='top', fill='both', expand='yes')


		# # Player input frame.
		# self.entry = Tk.Entry(self.mid_frame, width = 5)
		# self.enter_butt = Tk.Button(self.mid_frame, \
		# 							 text='Guess', command = self.play)
		# self.entry.pack(side = 'left')
		# self.enter_butt.pack(side = 'left')

		# # Guess tracking frame.
		# self.tracker = Tk.StringVar()
		# self.tracker_label = Tk.Label(self.track_frame, \
		# 							 textvariable = self.tracker)
		# self.tracker_label.pack(side = 'left')

		# Play and Quit frames.
		self.play_butt = Tk.Button(self.play_frame, text='Replay', \
			command = self.start)
		self.quit_butt = Tk.Button(self.quit_frame, text='Quit', 
			command = self.quit_now)
		self.play_butt.pack(side='left')
		self.quit_butt.pack(side='right')

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
		self.image = ImageTk.PhotoImage(Image.open('images/zombies2.jpg'))
		self.image_label.configure(image=self.image)


	def play(self):
		"""plays the game"""
		
				
	def quit_now(self):
		'''destroys the GUI'''
		self.main_window.destroy()


z = ZombieGame()


