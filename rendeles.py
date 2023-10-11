import szamla
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
            v_f_ar = f2_ar



