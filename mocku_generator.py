import random
import random


class T_shift:

    def shift(self, t, word):     
        return t[1:] + (word,)

class Rand_item:

    def __init__(self, gen_list = []) -> None:
        self.gen_list = gen_list
        

    def randomise_p(self, weighting, no_values):
        return random.choices(self.gen_list, weights = weighting, k = no_values)
        
class Mocku:

    def __init__(self):
        self.suffixes = {} 
        self.prefix = ()
        self.poet = []
        self.colour = []
        self.font = []

        # You will have to supply your own text files for this
        # to work.
        example_p = Rand_item(['marlowe.txt','shakespeare.txt', 'milton.txt','donne.txt', 'jonson.txt', 'pope.txt','herrick.txt', 'dryden.txt', 'shirley.txt', 'marvell.txt'])

        rand_p = example_p.randomise_p([1,5,7,9,11,12,13.75,13.75,13.75,13.75],1)

        for i in rand_p:
            self.poet.append(i)

        example_c = Rand_item(['copper','silver','gold', 'pallidium'])

        rand_c = example_c.randomise_p([60,30,8,2],1)

        for i in rand_c:
            self.colour.append(i)

        example_f = Rand_item(['nice','fancy','v. fancy', 'extremely fancy'])

        rand_f = example_f.randomise_p([60,30,8,2],1)

        for i in rand_f:
            self.font.append(i)
    

    def prep_file(self, order = 2):

        res = open(str(self.poet[0]))

        for line in res:
            for word in line.rstrip().split():
                self.prep_words(word, order)

    def prep_words(self, word, order = 2):

        tup = T_shift()

        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffixes[self.prefix].append(word)

        except KeyError:
            self.suffixes[self.prefix] = [word]

        self.prefix = tup.shift(self.prefix, word)               

    def make_text(self, n = 17):

        tup2 = T_shift()
        start = random.choice(list(self.suffixes.keys()))

        for i in range(n):
            suffixes_item = self.suffixes.get(start, None)
            if suffixes_item == None:
                self.make_text(n-1)
                return

            word = random.choice(suffixes_item)
            print(word, end=' ')
            start = tup2.shift(start, word)



if __name__ == '__main__':
    m = Mocku()
    m.prep_file()
    m.make_text()
    print(m.poet)
    print(m.colour)
    print(m.font)


