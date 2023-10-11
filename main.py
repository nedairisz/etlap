import etlap
import rendeles

etlap_meret = 60

etlap.cim("ÉTLAP", etlap_meret)

etlap.szoveg_kiiras("*", "Levesek", "*", etlap_meret)

etlap.megnevezes_osszeg("*", "Gulyás leves", "1800 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "Tojás leves", "1400 Ft", "*", etlap_meret)

etlap.szoveg_kiiras("*", "Főételek", "*", etlap_meret)

etlap.megnevezes_osszeg("*", "Lasagne", "2000 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "Rizottó", "1800 Ft", "*", etlap_meret)

etlap.cim("JÓ ÉTVÁGYAT!", etlap_meret)


kerdes1: str = input("Kér levest (I/N)? ")