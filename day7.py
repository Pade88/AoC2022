import pathlib
def partea_1(inputs):
    # Un 'dictionar' care sa contina toate path-urile (arbore)
    director_curent = pathlib.Path("/")
    # Un dictionar in care se stocheaza fisierele si se calculeaza dimensiunile
    system = dict()
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
                dimensiune, _ = line.split()
                # Poate merge cu default dict
                # Daca path-ul nu este in dictionar, il adaug, si adun dimensiunile fisierelor
                if director_curent not in system.keys():
                    system[director_curent] = 0
                    system[director_curent] += int(dimensiune)
                # Incep parcurgerea de jos in sus
                while director_curent != pathlib.Path("/"):
                    director_curent = director_curent.parent
                    # poate merge cu default dict?
                    if director_curent not in system.keys():
                        system[director_curent] = 0
                        system[director_curent] += int(dimensiune)

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