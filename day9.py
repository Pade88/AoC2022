import numpy
directii = {
    "U": numpy.array([-1, 0]),
    "D": numpy.array([1, 0]),
    "L": numpy.array([0, -1]),
    "R": numpy.array([0, 1]),
}

def miscare(cap, coada):
    di, dj = cap - coada
    # Daca diferenta de coordonate e 0, atunci nu am miscare
    if di == dj == 0:
        return False
    # Daca exista diferenta de coordonate, pe orice directie (abs)
    if abs(di) > 1 or abs(dj) > 1:
        coada[0] += numpy.sign(di)
        coada[1] += numpy.sign(dj)
    return True

def partea_1(my_inputs):
    noduri = [numpy.array([0, 0]) for _ in range(10)]
    v1 = {(0, 0)} # set in care pun pozitia de start (0, 0)
    for line in my_inputs:
        # recuperez directia si valoarea
        directia, cat = line.split()
        offset = directii[directia]
        # Ma deplasez
        for _ in range(int(cat)):
            noduri[0] += offset
            for i in range(9):
                # Daca nu am diferenta intre noduri, trec mai departe
                if not miscare(noduri[i], noduri[i + 1]):
                    break
            # Altfel adaug in set
            v1.add(tuple(noduri[1]))
    # returnez numarul punctelor unice vizitate
    return len(v1)


def partea_2(inputs):
    noduri = [numpy.array([0, 0]) for _ in range(10)]
    v1 = {(0, 0)}
    for line in my_inputs:
        directia, cat = line.split()
        offset = directii[directia]
        for _ in range(int(cat)):
            noduri[0] += offset
            for i in range(9):
                if not miscare(noduri[i], noduri[i + 1]):
                    break
            v1.add(tuple(noduri[-1]))
    # returnez numarul punctelor unice vizitate
    return len(v1)

if __name__ == "__main__":
    my_inputs = open("input_day_9.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')