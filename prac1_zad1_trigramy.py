__author__ = 'malaania'
import random

class WczytajTrigramy():

    @classmethod
    def wczytaj(cls, path,k):
        with open(path) as ngram_file:
            ngram_list = [next(ngram_file) for x in xrange(k)]
        return ngram_list

    @classmethod
    def zbuduj_slownik(cls,wczytana_lista,k):
        slownik = dict()
        for ln in wczytana_lista:
            line= ln.strip(" ").split(" ")
            if int(line[0])>k:
                key = line[1].rstrip(" ") + " " + line[2].rstrip(" ")
                value = line[3].rstrip("\n")
                if key in slownik:
                    slownik[key].append(value)
                else:
                    slownik[key]=[value]
        return slownik

    @classmethod
    def generuj_zdanie(cls, slownik):
        zdanie=''
        slowo = random.choice(slownik.keys())
        zdanie+=slowo
        while 1:
            if slowo in slownik:
                zdanie+=" "
                slowo = slowo.split(" ")[1]+" "+random.choice(slownik[slowo])
                zdanie+=slowo.split(" ")[1]
            else:
                break
        zdanie+="."
        return zdanie.capitalize()


slownik =  WczytajTrigramy.zbuduj_slownik(WczytajTrigramy.wczytaj("/home/malaania/Desktop/ngramy/3grams", 20000),5000)
zdanie = WczytajTrigramy.generuj_zdanie(slownik)
print zdanie
print len(slownik)