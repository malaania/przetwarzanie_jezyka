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
        while 1:
            if slowo in self.slownik:
                zdanie+=" "
                slowo = self.losuj_proporcjonalnie(self.slownik[slowo])
                zdanie+=slowo
                continue
            else:
                break
        if not zdanie.endswith("."):
            zdanie+="."
        return zdanie.capitalize()

    def generuj_tekst(self, liczba_zdan):
        tekst=""
        for i in range(0, liczba_zdan):
            tekst+= self.generuj_zdanie()
            tekst +=" "
        return tekst


class WczytajTrigramy():
    def __init__(self,path, k):
        ngram_list = []
        with open(path) as ngram_file:
            ngram_list = [next(ngram_file) for x in xrange(k)]
        slownik = dict()
        for ln in ngram_list:
            line= ln.strip(" ").split(" ")
            occurence = int(line[0])
            key = line[1].rstrip(" ") + " " + line[2].rstrip(" ")
            value = line[3].rstrip("\n")
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
        while 1:
            if slowo in self.slownik:
                zdanie+=" "
                slowo = slowo.split(" ")[1]+" "+self.losuj_proporcjonalnie(self.slownik[slowo])
                zdanie+=slowo.split(" ")[1]
            else:
                break
        if not zdanie.endswith("."):
            zdanie+="."
        return zdanie.capitalize()

    def generuj_tekst(self, liczba_zdan):
        tekst=""
        for i in range(0, liczba_zdan):
            tekst+= self.generuj_zdanie()
            tekst +=" "
        return tekst

costam =  WczytajBigramy("/home/malaania/Desktop/ngramy/2grams",10000)
print costam.generuj_zdanie()
costam3gramy = WczytajBigramy("/home/malaania/Desktop/ngramy/3grams",1000)
print costam3gramy.generuj_zdanie()
print costam.generuj_tekst(2)