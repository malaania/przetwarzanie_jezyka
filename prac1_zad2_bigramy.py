# -*- coding: utf8 -*-
import random

class WczytajBigramy():

    def __init__(self, path, k):
        ngram_list = []
        with open(path) as ngram_file:
            ngram_list = [next(ngram_file) for x in xrange(k)]
        slownik = dict()
        for ln in ngram_list:
            line= ln.strip(" ").split(" ")
            occurence = int(line[0])
            key = line[1].rstrip(" ")
            value = line[2].rstrip("\n")
            if key in slownik:
                  slownik[key][value] = occurence
            else:
                slownik[key]={ value:occurence}
        self.slownik = slownik

    def losuj_proporcjonalnie(self, sl):
        r = random.uniform(0, sum(sl.itervalues()))
        s = 0.0
        for k, v in sl.iteritems():
            s += v
            if r < s: return k
        return k

    def generuj_zdanie(self):
        zdanie=''
        slowo = random.choice(self.slownik.keys())
        zdanie+=slowo
        zdanie.capitalize()
        while 1:
            if slowo in self.slownik:
                zdanie+=" "
                slowo = self.losuj_proporcjonalnie(self.slownik[slowo])
                zdanie+=slowo
                continue
            else:
                break
        zdanie+="."
        return zdanie

costam =  WczytajBigramy("/home/malaania/Desktop/ngramy/2grams",10)
print costam.slownik["się"]
print costam.losuj_proporcjonalnie(costam.slownik["się"])
print costam.generuj_zdanie()