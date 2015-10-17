from _ast import Not
import random

__author__ = 'malaania'
class Slowo:
    def __init__(self,str):
        self.slowo = str
        self.nastepniki = []
    def dodaj_nastepnik(self, nast):
        self.nastepniki.append(nast)
    def __eq__(self, other):
        if isinstance(other,Slowo):
            return self.slowo == other.slowo
        return NotImplemented

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

    def generuj_zdanie1(self, slownik):
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
        return zdanie




    def zbuduj_liste_slow_i_nast(self, tab_nast):
        lista_slow_i_nast=[]
        for ln in tab_nast:
            line = ln.lstrip(" ").split(" ")
            temp_slowo = Slowo(line[1])
            temp_nastepnik = Slowo(line[2].rstrip("\n"))
            if temp_slowo in lista_slow_i_nast:
                temp_index_slowa = lista_slow_i_nast.index(temp_slowo)
                if temp_nastepnik in lista_slow_i_nast:
                    temp_index_nastep = lista_slow_i_nast.index(temp_nastepnik)
                    lista_slow_i_nast[temp_index_slowa].dodaj_nastepnik(lista_slow_i_nast[temp_index_nastep])
                else:
                    lista_slow_i_nast.append(temp_nastepnik)
                    lista_slow_i_nast[temp_index_slowa].dodaj_nastepnik(lista_slow_i_nast[-1])
            else:
                lista_slow_i_nast.append(temp_slowo)
                lista_slow_i_nast.append(temp_nastepnik)
                lista_slow_i_nast[-2].dodaj_nastepnik(lista_slow_i_nast[-1])
        return lista_slow_i_nast

    def generuj_zdanie(self, lista):
        zdanie = ''
        temp = random.choice(lista)
        zdanie+=temp.slowo
        zdanie
        while len(temp.nastepniki) != 0:
            temp = random.choice(temp.nastepniki)
            zdanie+=" "
            zdanie+=temp.slowo
        zdanie+=". "
        return zdanie.capitalize()

    def generuj_tekst(self, lista, il_zdan):
        tekst=""
        for i in range(0, il_zdan):
            tekst+= self.generuj_zdanie(lista)
        return tekst

wczytaj = WczytajNGram()
wczytane_gramy = wczytaj.wczytaj("/home/malaania/Desktop/ngramy/2grams",1000)
sl = wczytaj.zbuduj_slownik(wczytane_gramy)
print wczytaj.generuj_zdanie1(sl)
#for k,va in sl.iteritems():
#    print k
#    print len(sl[k])
#lista_sl_i_nast = wczytaj.zbuduj_liste_slow_i_nast(wczytane_gramy)
#print wczytaj.generuj_tekst(lista_sl_i_nast,5)
