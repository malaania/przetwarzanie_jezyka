__author__ = 'malaania'

import random

class WczytajNGram():
    def wczytaj(self, path, k):
        with open(path) as ngram_file:
            ngram_list = [next(ngram_file) for x in xrange(k)]
        return ngram_list

    def zbuduj_slownik(self,wczytana_lista):
        slownik=dict()
        for ln in wczytana_lista:
            line= ln.strip(" ").split(" ")
            temp_slowo= line[1].rstrip(" ")
            temp_nastepnik = line[2].rstrip("\n")
            if temp_slowo in slownik:
                slownik[temp_slowo].append(temp_nastepnik)
            else:
                slownik[temp_slowo]=[temp_nastepnik]
        return slownik

    def generuj_zdanie(self, slownik):
        zdanie=''
        slowo = random.choice(slownik.keys())
        zdanie+=slowo
        zdanie.capitalize()
        while 1:
            if slowo in slownik:
                zdanie+=" "
                slowo = random.choice(slownik[slowo])
                zdanie+=slowo
                continue
            else:
                break
        zdanie+="."
        return zdanie.capitalize()

    def generuj_tekst(self, lista, il_zdan):
        tekst=""
        for i in range(0, il_zdan):
            tekst+= self.generuj_zdanie(lista)
            tekst +=" "
        return tekst

wczytaj = WczytajNGram()
wczytane_gramy = wczytaj.wczytaj("/home/malaania/Desktop/ngramy/2grams",10000)
sl = wczytaj.zbuduj_slownik(wczytane_gramy)
print wczytaj.generuj_zdanie(sl)
print wczytaj.generuj_tekst(sl,4)
#for k,va in sl.iteritems():
#    print k
#    print len(sl[k])
#lista_sl_i_nast = wczytaj.zbuduj_liste_slow_i_nast(wczytane_gramy)
#print wczytaj.generuj_tekst(lista_sl_i_nast,5)
