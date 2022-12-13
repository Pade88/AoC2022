def compare(nr1, nr2):
    if isinstance(nr1, int):
        if isinstance(nr2, int):
            # Ambele int
            return nr1 - nr2
        else:
            # Doar al doilea int
            return compare([nr1], nr2)
    else:
        # Doar primul int
        if isinstance(nr2, int):
            return compare(nr1, [nr2])
    # Parcurgere
    for a, b in zip(nr1, nr2):
        if compare(a, b):
            return compare(a, b)
    
    return len(nr1) - len(nr2)


def partea_1(my_inputs):
    my_inputs = list(map(str.splitlines, my_inputs.split('\n\n')))
    counter = 0
    for idx, (a, b) in enumerate(my_inputs):
        a, b = eval(a), eval(b) # lista la string
        if compare(a, b) < 0:
            counter += idx + 1
    return counter

def partea_2(my_inputs):
    # lista la string
    my_inputs = list(map(eval, my_inputs.split()))
    # 0 - idx2 1 - idx6
    idx = [1, 2]
    for val in my_inputs:
        # > 2 creste si idx2 si idx6
        if compare(val, [[2]]) < 0:
            idx[0] += 1
            idx[1] += 1
        # Doar idx6
        elif compare(val, [[6]]) < 0:
            idx[1] += 1

    import math
    # idx2 * idx2
    return math.prod(idx)

if __name__ == "__main__":
    my_inputs = open("input_day_13.txt", "r").read().strip()
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')