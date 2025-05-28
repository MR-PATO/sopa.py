from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# Sopa de letras como lista de listas (cada sublista es una fila)
sopa = [
    list("ACCIOPEMAFCBNM"),
    list("IGBNEGQBARSTOP"),
    list("NEOURFNZEDOVMS"),
    list("TBKVDUEGAUDEFI"),
    list("EFLWVZVMYIGBC"),
    list("LORN RFNBENOKRO"),
    list("IGCEUEZFZLWMEL"),
    list("GMCRVKPLURFBWO"),
    list("EOZYFMSCÑDZNFG"),
    list("NBXWCÑIUOVEOXI"),
    list("COANVHC KWEAIYA"),
    list("ISGFEB OEANBCMD"),
    list("AWXVDILCFYGANE"),
    list("EJKLKUORSDZLAL"),
    list("MOGNCYGURECICA"),
    list("ONOBTWOKMTEC"),
    list("CSHSWRAKANBSYO"),
    list("IXYEFEGVW RVETN"),
    list("OZTLOHOC LAW DOD"),
    list("NVRSUNMCVBROP U"),
    list("ABCKBWUNANATKC"),
    list("LZRF DQAEÑYULC"),
    list("CLGLRPZLOVKAÑI"),
    list("SDSKWEYCB CZSFO"),
    list("GKZOBIGORUNBWN"),
    list("VLBA GOVJÑUODGE"),
    list("DFC ESFMISJKFMS"),
    list("SEGUNDAFASEACF")
]

# Coordenadas de letras que forman las palabras a resaltar (basadas en imagen)
# Formato: (fila, columna) empezando desde 0

coordenadas_verdes = set([
    # INTELIGENCIA EMOCIONAL (vertical)
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
    (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0),
    (14, 0), (15, 0), (16, 0), (17, 0),

    # SIMULADOR (diagonal descendente izquierda)
    (2, 14), (3, 13), (4, 12), (5, 11), (6, 10), (7, 9), (8, 8), (9, 7), (10, 6),

    # PSICOLOGÍA (vertical)
    (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12), 

    # VIAL (vertical)
    (14, 13), (15, 13), (16, 13), (17, 13),

    # CABEZA (horizontal)
    (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),

    # OIDO (vertical)
    (9, 19), (10, 19), (11, 19), (12, 19),

    # ALCOHOL (horizontal inversa)
    (17, 16), (17, 15), (17, 14), (17, 13), (17, 12), (17, 11), (17, 10),

    # AUTOCERVECERIA (diagonal descendente derecha)
    (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8),
    (10, 9), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15),

    # CERVEZA (vertical)
    (24, 6), (25, 6), (26, 6), (27, 6), (28, 6), (29, 6), (30, 6),

    # ESTRES (horizontal)
    (21, 14), (21, 15), (21, 16), (21, 17), (21, 18), (21, 19)
])

# Mostrar la sopa con colores
for i, fila in enumerate(sopa):
    for j, letra in enumerate(fila):
        if (i, j) in coordenadas_verdes:
            print(Fore.GREEN + letra, end=' ')
        else:
            print(Style.RESET_ALL + letra, end=' ')
    print()  # Salto de línea por fila
