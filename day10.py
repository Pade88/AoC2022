sum = 0
# Creez o matrice plina de @ (40 x 6)
grafica = [['@' for _ in range(40)] for _ in range(6)]

def iteratie(counter, X):
    global sum
    global grafica
    _cnt = counter - 1
    # Partea 2
    if abs(X-(_cnt%40))<=1:
        # Pixel luminat, cand contorul%40 e mai mare decat valoarea stocata in X
        grafica[_cnt//40][_cnt%40] = '#'
    else:
        # Pixel inchis
        grafica[_cnt//40][_cnt%40] = '.'
    # Partea 1
    # Incrementez suma cu contor * X daca conotorul are valorile din list
    if counter in [20, 60, 100, 140, 180, 220]:
        sum += X*counter

def partea_1(my_inputs):
    cycle_count = 0
    X = 1
    global sum
    # Iterez
    for cmd in my_inputs:
        if "noop" in cmd:
            # La noop doar cresc contorul
            cycle_count += 1
            iteratie(cycle_count, X)
        else:
            # La add recuperez valoarea, cresc contorul de 2 ori si incrementez registrul
            numar = int(cmd.split()[-1])
            cycle_count += 1
            iteratie(cycle_count, X)
            cycle_count += 1
            iteratie(cycle_count, X)
            X += numar
    # Sum e globala (TBU)
    return sum

def partea_2(my_inputs):
    # iterez cele 6 linii de caractere si le printez sub forma de string
    for char in range(6):
        print(''.join(grafica[char]))

if __name__ == "__main__":
    my_inputs = open("input_day_10.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')