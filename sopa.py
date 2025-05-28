# sopa_coloreada.py

def mostrar_sopa():
    sopa = [
        list("ACCIOPEMAFCBNM"),
        list("IGBNEGQBARSTOP"),
        list("NEOURFNZEDOVMS"),
        list("TBKVDUEGAUDEFI"),
        list("EFLWVZVMYIGGBC"),
        list("LORNRFNBENOKRO"),
        list("IGCEUEZFZLWMEL"),
        list("GMCRVKPLURFBWO"),
        list("EOZYFMSCÑDZNFG"),
        list("NBXWCÑIUOVEOXI"),
        list("COANVHCKWEAIYA"),
        list("ISGFEBEOANBCMD"),
        list("AWXVDILCFYGANE"),
        list("EJKLKUORSDZLAL"),
        list("MOGNCYGLRECICA"),
        list("ONJOBTIWOKMTEC"),
        list("CSHSWRAKANBSYO"),
        list("IXYEFEGVWRVETN"),
        list("OZTLOHOCLAWDOD"),
        list("NVRSUNMCVBROPX"),
        list("ABCKBWUNANATKC"),
        list("LZRFDQOAEÑYULC"),
        list("CLGLRPZLOVKAÑI"),
        list("SDSKWEYCBCZSFO"),
        list("GKZOBIGORUNBWN"),
        list("VLBA GOVJÑUODGE"),
        list("DFCESFMISJKFMS"),
        list("SEGUNDAFASEACF"),
    ]

    # Coordenadas corregidas de todas las palabras
    coordenadas = set([
        # 1. INTELIGENCIAEMOCIONAL (vertical)
        *[(i, 0) for i in range(18)],

        # 2. SIMULADOR (diagonal invertida desde (2,14) a (10,6))
        (2,14),(3,13),(4,12),(5,11),(6,10),(7,9),(8,8),(9,7),(10,6),

        # 3. PSICOLOGIA (columna 12, de (5,12) a (13,12))
        *[(i,12) for i in range(5,14)],

        # 4. VIAL (vertical desde (14,13) a (17,13))
        (14,13),(15,13),(16,13),(17,13),

        # 5. CABEZA (horizontal desde (0,5) a (0,10))
        (0,5),(0,6),(0,7),(0,8),(0,9),(0,10),

        # 6. OIDO (vertical desde (9,13) a (12,13))
        (9,13),(10,13),(11,13),(12,13),

        # 7. ALCOHOL (horizontal invertida desde (17,16) a (17,10))
        *[(17,i) for i in range(10,17+1)][::-1],

        # 8. AUTOEMBRIAGUEZ (diagonal desde (10,0))
        (10,0),(11,1),(12,2),(13,3),(14,4),(15,5),(16,6),(17,7),(18,8),(19,9),(20,10),(21,11),

        # 9. CERVEZA (horizontal desde (24,3) a (24,9))
        *[(24,i) for i in range(3,10)],

        # 10. ESTRÉS (palabra ES y luego TRES – letras dispersas)
        (1,13),(1,14),  # ES
        (26,0),(26,1),(26,2),(26,3)  # TRES
    ])

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
