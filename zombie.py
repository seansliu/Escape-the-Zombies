# Escape the Zombie backend functions
#
# Michelle Lee, Sean Liu, Sophie Lucy

import random


def index_dict(dictfile_name):
	"""index and return the dictionary"""
	dictfile = open(dictfile_name,'r')
	index = {}
	for line in dictfile:
		word = line.strip()
		wlen = len(word)
		if wlen not in index:
			index[wlen] = [word]
		else:
			index[wlen].append(word) 

	return index
	

def generate_word(wordbank, level):
	"""generate random number according to level"""
	while 1:
		if level == 0:		# easy
			num = random.randint(3,9)
		elif level == 1:	# medium
			num = random.randint(10,14)
		else:				# hard
			num = random.randint(15,18)
		if num in wordbank:
			break
	return random.choice(wordbank[num])
