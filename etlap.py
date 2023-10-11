def jelekkelkiiras(jel, db):
    print(jel * db)

def cim(szoveg, etlap_meret):
    jelekkelkiiras("*", etlap_meret)
    szoveg_kiiras("*", szoveg, "*", etlap_meret)
    jelekkelkiiras("*", etlap_meret)

def szoveg_kiiras(jel, szoveg, jel2, etlap_meret):
    hossz: int = etlap_meret - len(jel) - len(jel2)
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def megnevezes_osszeg(jel, szoveg, szam, jel3, etlap_meret):
    hossz: int = int (etlap_meret /3)
    ures: str = "."
    print(f"{jel}{szoveg:>{hossz}}{ures*hossz}{szam:<{hossz}}{jel3}")
