
with open("egzai_test/duomenys.txt", "r", encoding="utf-8") as f:
    pamokos = {}
    for line in f:
        dalys = line.split()

        vardai = dalys[0]
        pamoka = dalys[1]
        kiekis = int(dalys[2])
        paz = list(map(int, dalys[3:3 + kiekis]))

        vidur = sum(paz) / kiekis

        if vidur < 9:
            if pamoka not in pamokos:
                pamokos[pamoka] = []
            pamokos[pamoka].append(vardai)

with open("egzai_test/rezultatai.txt", "w", encoding="utf-8") as f:
    for pam in pamokos:
        f.write(f"{pam} {len(pamokos[pam])}\n")
        for vardaz in pamokos[pam]:
            f.write(f"{vardaz}\n")
