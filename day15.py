import re

def partea_1(my_inputs):
    # Regex sa obtin doar coordonatele (d+)
    obs = [tuple(map(int, re.findall(r"-?\d+", observation))) for observation in my_inputs]
    
    output = list()
    # Prin fiecare tupla de coordonate calculez diferentele intre x, y si y 2000000
    for sen_x, sen_y, beacon_x, beacon_y in obs:
        d = abs(sen_x - beacon_x) + abs(sen_y - beacon_y) - abs(sen_y - 2000000)
        if d >= 0:
            # Adaug doar pozitivele
            output.append((sen_x - d, sen_x + d))
    
    # toate coordonatele pozitive
    x = set.union(*[set(range(a, b + 1)) for a, b in output])
    # In y ajunge doar beacon_x acolo unde beacon y = 2000000
    y = set(beacon_x for *_, beacon_x, beacon_y in obs if beacon_y == 2000000)

    return len(x - y)

def partea_2(my_inputs):
    pass

if __name__ == "__main__":
    my_inputs = open("input_day_15.txt", "r").read().strip().split("\n")
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')