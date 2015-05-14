# Escape the Zombie backend functions
#
# Michelle Lee, Sean Liu, Sophie Lucy

import random


def index_dict():
    """index and return the dictionary"""
    dictfile = open('/usr/share/dict/words','r')
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
    if level == 0:      # easy
            num = random.randint(2,7)
    elif level == 1:    # medium
            num = random.randint(8,14)
    else:               # hard
            num = random.randint(17,23)

    # generate random word from number
    return random.choice(wordbank[num])
