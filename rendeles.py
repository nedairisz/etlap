import szamla
"""
def rendeles(l1, l1_ar, l2, l2_ar, f1, f1_ar, f2, f2_ar):

    valasztott_leves=""
    valasztott_foetel=""
    v_l_ar =0
    v_f_ar =0

    kerdes1: str = input("Kér levest I/N ? ")
    if kerdes1 == "I" or kerdes1 == "i" or kerdes1 == "igen" or kerdes1 == "Igen":
        valasz1: str = input("Melyik levest kéri 1/2 ? ")
        if valasz1 == "1":
            valasztott_leves = l1
            v_l_ar = l1_ar
        elif valasz1 == "2":
            valasztott_leves = l2
            v_l_ar = l2_ar

    
    kerdes2: str = input("Kér főételt I/N ? ")
        if kerdes2 == "I" or "i" or "igen" or "Igen":
            valasz2: str = input("Melyik főételt kéri 1/2 ? ")
            if valasz2 == "1":
                valasztott_foetel = f1
                v_f_ar = f1_ar
            elif valasz2 == "2":
                valasztott_foetel = f2
                v_f_ar = f2_ar"""



kerdes_leves: list = ["Kér levest I/N?: ", "Melyik levest kéri 1/2 ? "]
kerdes_foetel: list = ["Kér főételt I/N?: ", "Melyik főételt kéri 1/2 ? "]

def rendeles(kerdes):
    valasztott: list = []
    ker: str = input(kerdes[0])
    while not(ker =="I" or ker =="N"):
        print("Hiba! Csak I/N válasz adható!")
        ker: str = input(kerdes[0])
    if ker == "I":
        melyik: str = input(kerdes[1])
        while not(melyik== "1" or melyik== "2"):
            print("Hiba! Csak 1/2 válasz adható!")
            melyik: int = int(input(kerdes[1]))
        print([melyik-1])

    return melyik-1
