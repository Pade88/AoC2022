def partea_1(inputs):
    # Desenez harta
    head = (0, 0)
    tail = [(0, 0) for _ in range(15)]
    for line in my_inputs:
        directia, cat = line.split()

def partea_2(inputs):
    import numpy
    directii = {
    "U": numpy.array([-1, 0]),
    "D": numpy.array([1, 0]),
    "L": numpy.array([0, -1]),
    "R": numpy.array([0, 1]),
    }

    def parse(in_line):
        # convertesc directia de deplasare si valoarea
        directia, cat = in_line.split()
        cat = int(cat)
        return directii[directia], cat

    def miscare(cap, coada):
        # Schimb coordonatele capului si coadei
        # sign returneaza -1, sau 1 in functie de tipul miscarii
        di, dj = cap - coada
        if di == 0 and abs(dj) >= 2:
            coada[1] += numpy.sign(dj)
        elif dj == 0 and abs(di) >= 2:
            coada[0] += numpy.sign(di)
        elif not (abs(di) <= 1 and abs(dj) <= 1):
            coada[0] += numpy.sign(di)
            coada[1] += numpy.sign(dj)

    dimensiune_harta = 10
    vizitat = set() # fara duplicate in punctele vizitate
    # Desenez harta cu 0 de puncte (x, y)
    harta = [numpy.array([0, 0]) for _ in range(dimensiune_harta)]

    for line in inputs:
        # recuperez directia si valoarea
        directia, cat = parse(line)
        for _ in range(cat):
            # adaug ultimul punct in setul de puncte vizitate
            vizitat.add(tuple(harta[-1]))
            # setez directia
            harta[0] += directia
            # deplasez capul si coada
            for i in range(dimensiune_harta - 1):
                miscare(harta[i], harta[i + 1])
    # returnez numarul punctelor unice vizitate
    return len(vizitat)

if __name__ == "__main__":
    my_inputs = open("input_day_9.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')