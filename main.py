import etlap

etlap_meret = 60

etlap.cim("ÉTLAP", etlap_meret)

etlap.szoveg_kiiras("*", "Levesek", "*", etlap_meret)

etlap.megnevezes_osszeg("*", "1. Gulyás leves", "1800 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "2. Tojás leves", "1400 Ft", "*", etlap_meret)

etlap.szoveg_kiiras("*", "Főételek", "*", etlap_meret)

etlap.megnevezes_osszeg("*", "1. Lasagne", "2000 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "2. Rizottó", "1800 Ft", "*", etlap_meret)

etlap.cim("JÓ ÉTVÁGYAT!", etlap_meret)

import rendeles
rendeles.rendeles("1. Gulyás leves", "1800 Ft", "2. Tojás leves", "1400 Ft", "1. Lasagne", "2000 Ft", "2. Rizottó", "1800 Ft")



