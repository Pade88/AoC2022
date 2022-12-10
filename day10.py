sum = 0
grafica = [['@' for _ in range(60)] for _ in range(10)]

def iteratie(counter, X):
    global sum
    global grafica
    _cnt = counter - 1
    if abs(X-(_cnt%40))<=1:
        grafica[_cnt//40][_cnt%40] = '#'
    else:
        grafica[_cnt//40][_cnt%40] = '.'
    if counter in [20, 60, 100, 140, 180, 220]:
        sum += X*counter

def partea_1(my_inputs):
    cycle_count = 0
    X = 1
    global sum
    for cmd in my_inputs:
        if "noop" in cmd:
            cycle_count += 1
            iteratie(cycle_count, X)
        else:
            numar = int(cmd.split()[-1])
            cycle_count += 1
            iteratie(cycle_count, X)
            cycle_count += 1
            iteratie(cycle_count, X)
            X += numar
    return sum

def partea_2(my_inputs):
    for char in range(6):
        print(''.join(grafica[char]))

if __name__ == "__main__":
    my_inputs = open("input_day_10.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')