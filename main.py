import etlap
import rendeles
import szamla

leves  = ["1. Gulyás leves", "2. Tojás leves"]
foetel= ["1. Lasagne", "2. Rizottó",]
leves_ar = (1800, 1400)
foetel_ar= (2000, 1800)

etlap_meret = 60

def lista_kiir(lista,lista_ar):
    i:int = 0
    while i < len(lista):
        etlap.megnevezes_osszeg("*", lista[i], str(lista_ar[i]) + "Ft", "*", etlap_meret)
        i += 1

etlap.cim("ÉTLAP", etlap_meret)
etlap.szoveg_kiiras("*", "Levesek", "*", etlap_meret)
lista_kiir(leves, leves_ar)
etlap.szoveg_kiiras("*", "Főételek", "*", etlap_meret)
lista_kiir(foetel, foetel_ar)
etlap.cim("JÓ ÉTVÁGYAT!", etlap_meret)

kerdes_leves: list = ["Kér levest I/N?: ", "Melyik levest kéri 1/2 ? ", "Nincsen leves rendelve."]
kerdes_foetel: list = ["Kér főételt I/N?: ", "Melyik főételt kéri 1/2 ?", "Nincsen főétel endelve."]

valasztott = rendeles.rendeles(kerdes_leves)
print(valasztott)
if valasztott is not None:
        print(leves[valasztott])

valasztott = rendeles.rendeles(kerdes_foetel)
print(valasztott)
if valasztott is not None:
        print(foetel[valasztott])



etlap.cim("NYUGTA", etlap_meret)
etlap.szoveg_kiiras("*", "Rendelése:", "*", etlap_meret)

def nyugta_kiir(lista,lista_ar):
    i:int = 0
    while i < len(lista):
        etlap.megnevezes_osszeg("*", lista[valasztott], str(lista_ar[i]) + "Ft", "*", etlap_meret)
        i += 1

nyugta_kiir(leves, leves_ar)
nyugta_kiir(foetel, foetel_ar)
etlap.jelekkelkiiras(" ", etlap_meret)


etlap.megnevezes_osszeg("*", "Összesen:", (lista_ar[i]) + "Ft", "*", etlap_meret)
etlap.cim("KÖSZÖNJÜK!", etlap_meret)