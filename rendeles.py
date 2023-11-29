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

leves  = ["1. Gulyás leves", "2. Tojás leves"]
foetel= ["1. Lasagne", "2. Rizottó",]
leves_ar = (1800, 1400)
foetel_ar= (2000, 1800)

kerdes_leves: list = ["Kér levest I/N?: ", "Melyik levest kéri 1/2 ? "]
kerdes_foetel: list = ["Kér főételt I/N?: ", "Melyik főételt kéri 1/2 ? "]

def rendeles(kerdes_leves):
    valasztott: list = []
    ker: str = input(kerdes_leves[0])
    while not(ker =="I" or ker =="N"):
        print("Hiba! Csak I/N válasz adható!")
        ker: str = input(kerdes_leves[0])
    if ker == "I":
        melyik: str = input(kerdes_leves[1])
        while not(melyik== "1" or melyik== "2"):
            print("Hiba! Csak 1/2 válasz adható!")
            melyik: str = input(kerdes_leves[1])
        if melyik == "1":
            valasztott.append(leves[0])
        elif melyik == "2":
            valasztott.append(leves[1])  
    elif ker == "N":
        sys.exit()


    print(valasztott)
    