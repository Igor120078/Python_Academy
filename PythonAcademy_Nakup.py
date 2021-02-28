from pprint import pprint as pp

POTRAVINY = {'banan': 30,
             'chleb': 20,
             'jablko': 10,
             'jogurt': 10,
             'maso': 100,
             'mleko': 30,
             'pomeranc': 15}

ODDELOVAC = '=' * 40
print(ODDELOVAC)
pp(POTRAVINY)
print(ODDELOVAC)

KOSIK = {}
nakup = True
while nakup:
    vyber_n = input(f"VYBERTE ZBOZI (AKTUALNI POCET: {len(KOSIK)}): ")
    if vyber_n == "q":
        nakup = False
    else:
        KOSIK[vyber_n] = POTRAVINY.get(vyber_n, 0)

else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI ...")
    print(KOSIK)
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(f"CENA CELKEM: {CELKEM} CZK")