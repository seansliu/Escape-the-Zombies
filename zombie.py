# Escape the Zombie backend functions
#
# Michelle Lee, Sean Liu, Sophie Lucy

import random

class zomb:
    
    def __init__(self):
        self.dictionary = dict()
        
    #make new dict with all words in dictionary
    def index_dict(self):
        
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
                
    def generate_word(self, level):
        #generate random number according to level
        if level == 0:
                num = random.randint(2,7)
        elif level == 1:
                num = random.randint(8,14)
        else:
                num = random.randint(17,23)

        #generate random word from number
        ranword = random.choice(self.dictionary[num])

        return ranword
    
# others...

