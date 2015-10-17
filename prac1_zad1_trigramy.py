__author__ = 'malaania'

class WczytajTrigramy():

    @classmethod
    def wczytaj(cls, path):
        with open(path) as ngram_file:
            ngram_list = [next(ngram_file) for x in xrange(k)]
        return ngram_list

    @classmethod
    def zbuduj_slownik(cls,wczytana_lista):
        slownik = dict()
        for ln in wczytana_lista:
            line= ln.strip(" ").split(" ")
            key = line[1].rstrip(" ") + " " + line[2].rstrip(" ")
            value = line[3].rstrip("\n")
        if key in slownik:
            slownik[key].append(value)
        else:
            slownik[key]=[value]
        return slownik

slownik =  WczytajTrigramy.zbuduj_slownik(WczytajTrigramy.wczytaj("/home/malaania/Desktop/ngramy/2grams"))
for i in slownik["do domu"]:
    print i

