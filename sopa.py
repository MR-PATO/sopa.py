# resaltador_sopa.py

def mostrar_sopa():
    sopa = [
        list("ACCIOPEMAFCBNM"),
        list("IGBNEGQBARSTOP"),
        list("NEOURFNZEDOVMS"),
        list("TBKVDUEGAUDEFI"),
        list("EFLWVZVMYIGBC"),
        list("LORNRFNBENOKRO"),
        list("IGCEUEZFZLWMEL"),
        list("GMCRVKPLURFBWO"),
        list("EOZYFMSCÑDZNFG"),
        list("NBXWCÑIUOVEOXI"),
        list("COANVHCKWEAIYA"),
        list("ISGFEBEOANBCMD"),
        list("AWXVDILCFYGANE"),
        list("EJKLKUORSDZLAL"),
        list("MOGNCYGURECICA"),
        list("ONOBTWOKMTECZZ"),
        list("CSHSWRAKANBSYO"),
        list("IXYEFEGVWRVETN"),
        list("OZTLOHOCLAWDOD"),
        list("NVRSUNMCVBROPX"),
        list("ABCKBWUNANATKC"),
        list("LZRFDQAEÑYULCC"),
        list("CLGLRPZLOVKAÑI"),
        list("SDSKWEYCBCZSFO"),
        list("GKZOBIGORUNBWN"),
        list("VLBA GOVJÑUODGE"),
        list("DFC ESFMISJKFMS"),
        list("SEGUNDAFASEACF")
    ]

    coordenadas = {
        # Ejemplo: (fila, columna)
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
        (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0),
        (14, 0), (15, 0), (16, 0), (17, 0),  # INTELIGENCIA EMOCIONAL

        (2, 14), (3, 13), (4, 12), (5, 11), (6, 10), (7, 9), (8, 8),
        (9, 7), (10, 6),  # SIMULADOR

        (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12),
        (12, 12), (13, 12),  # PSICOLOGIA

        (14, 13), (15, 13), (16, 13), (17, 13),  # VIAL

        (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),  # CABEZA

        (9, 13), (10, 13), (11, 13), (12, 13),  # OIDO

        (17, 16), (17, 15), (17, 14), (17, 13), (17, 12), (17, 11), (17, 10),  # ALCOHOL

        (26, 0), (26, 1), (26, 2), (26, 3), (26, 4), (26, 5), (26, 6), (26, 7),
        (26, 8), (26, 9), (26, 10),  # SEGUNDAFASE
    }

    print("SOPA DE LETRAS CON PALABRAS RESALTADAS:\n")

    for i, fila in enumerate(sopa):
        for j, letra in enumerate(fila):
            if (i, j) in coordenadas:
                print(f"\033[92m{letra}\033[0m", end=' ')  # Verde
            else:
                print(letra, end=' ')
        print()

if __name__ == "__main__":
    mostrar_sopa()
    input("\nPresiona Enter para salir...")
