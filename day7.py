import pathlib


# Solutie: parcurg linie cu linie, cand intalnesc comanda de $ cd, in functie de argument, creez un obiect
# PosixPath (pot sa folosesc / pentru a compune un path, si .parent pentru a stabilii radacina)
# Folosesc un defaultdict (nu ridica keyerror) si stochez fiecare path : dimensiunea fisierelor din el
# Pentru partea 1 si 2, doar parcurg dictionarul si fac operatii cu dimensiunile fisierelor.

def partea_1(inputs):
    # Un 'dictionar' care sa contina toate path-urile (arbore)
    director_curent = pathlib.Path("/")
    # Un dictionar in care se stocheaza fisierele si se calculeaza dimensiunile
    from collections import defaultdict
    system = defaultdict(int)
    # parcurgem liniile
    for line in inputs:
        # Switch pentru fiecare comanda care incepe cu $
        match line[0]:
            # Caz ls - cd
            case "$":
                _, cmd, *argument = line.split()
                # schimbam directorul un functie de argumentul de la cd
                if cmd == "cd":
                    # Creez root-ul fsului
                    if argument[0] == "/":
                        director_curent = pathlib.Path("/")
                    # Ma intorc la radacina (parent)
                    elif argument[0] == "..":
                        director_curent = director_curent.parent
                    # Compun path-ul
                    else:
                        director_curent = director_curent / argument[0]
            # Caz dir x
            case "d":
                ...
            # Caz dimensiune file - output de la ls
            case _:
                dimensiune = line.split()[0]
                # copiez posix-ul director_curent pentru a nu-l suprascrie !!!
                _cpy = director_curent
                # Daca path-ul nu este in dictionar, il adaug, si adun dimensiunile fisierelor
                # Cu defaultdict pot sa adun direct, fara sa mai verific daca _cpy este in dict
                system[_cpy] += int(dimensiune)
                # Incep parcurgerea de jos in sus
                while _cpy != pathlib.Path("/"):
                    _cpy = _cpy.parent
                    # poate merge cu default dict?
                    system[_cpy] += int(dimensiune)
    suma = 0
    for dimensiune in system.values():
        if dimensiune <= 100000:
            suma += dimensiune
    return suma, system

def partea_2(system):
    # primesc sistemul de fisiere
    tmp_list = list()
    # dimensiunea radacinii
    radacina = system.get(pathlib.Path("/"))
    for dimensiune in system.values():
        if dimensiune >= 30000000 - (70000000 - radacina):
            tmp_list.append(dimensiune)
    # Returnez minimul din lista
    return min(tmp_list)

if __name__ == "__main__":
    my_inputs = open("input_day_7.txt", "r").read().split("\n")
    sol_1, sis = partea_1(my_inputs)
    print(f'Solutia partea 1: {sol_1}')
    print(f'Solutia partea 2: {partea_2(sis)}')