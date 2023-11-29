import etlap

leves  = ["1. Gulyás leves", "2. Tojás leves"]
foetel= ["1. Lasagne", "2. Rizottó",]
leves_ar = (1800, 1400)
foetel_ar= (2000, 1800)

etlap_meret = 60

etlap.cim("ÉTLAP", etlap_meret)
etlap.szoveg_kiiras("*", "Levesek", "*", etlap_meret)

def lista_kiir(lista,lista_ar):
    i:int = 0
    while i < len(lista):
        etlap.megnevezes_osszeg("*", lista[i], str(lista_ar[i]) + "Ft", "*", etlap_meret)
        i += 1

lista_kiir(leves, leves_ar)
etlap.szoveg_kiiras("*", "Főételek", "*", etlap_meret)
lista_kiir(foetel, foetel_ar)
etlap.cim("JÓ ÉTVÁGYAT!", etlap_meret)

#etlap.megnevezes_osszeg("*", "1. Gulyás leves", "1800 Ft", "*", etlap_meret)
#etlap.megnevezes_osszeg("*", "2. Tojás leves", "1400 Ft", "*", etlap_meret)

import rendeles
valasztott = rendeles.rendeles(kerdes_leves)
print(valasztott)





