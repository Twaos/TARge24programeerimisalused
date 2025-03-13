import random

nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))

if vanus < 5:
    for _ in range(3):
        print(f"Tere, {nimi}!")
else:
    arv_tehteid = len(nimi)
    tehted = []
    vastused = []
    kasutaja_vastused = []
    oiged_vastused = 0

    for _ in range(arv_tehteid):
        arv1 = random.randint(1, 10)
        arv2 = random.randint(1, 10)
        tehe = random.choice(['+', '-', '*'])

        if tehe == '+':
            oige_vastus = arv1 + arv2
            tehted.append(f"{arv1} + {arv2} = ?")
        elif tehe == '-':
            oige_vastus = arv1 - arv2
            tehted.append(f"{arv1} - {arv2} = ?")
        else:
            oige_vastus = arv1 * arv2
            tehted.append(f"{arv1} * {arv2} = ?")

        vastused.append(oige_vastus)
        kasutaja_vastus = int(input(f"{tehted[-1]} "))
        kasutaja_vastused.append(kasutaja_vastus)

    for i in range(arv_tehteid):
        if kasutaja_vastused[i] == vastused[i]:
            print(f"{tehted[i]} Õige!")
            oiged_vastused += 1
        else:
            print(f"{tehted[i]} Vale! Õige vastus on {vastused[i]}.")

    if oiged_vastused == arv_tehteid:
        print(f"Tubli, {nimi}! Said kõik {arv_tehteid} tehet õigesti!")
    elif oiged_vastused > 0:
        print(f"Hästi läks, {nimi}! Said {oiged_vastused} tehet õigesti.")
    else:
        print(f"Proovi veel, {nimi}! Ära heida meelt.")