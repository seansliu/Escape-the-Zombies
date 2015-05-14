# Escape the Zombie backend functions
#
# Michelle Lee, Sean Liu, Sophie Lucy

import random


def index_dict():
    """index and return the dictionary"""
    dictfile = open('/usr/share/dict/words','r')
    dictlist = dictfile.readlines()
    
    for line in dictlist:
        word = line.strip()
        wlen = len(word)
        
        if wlen not in self.dictionary:
            self.dictionary[wlen] = [word]
            print wlen, word
            
        else:
            self.dictionary[wlen].append(word) 

    return self.dictionary
    

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
    

