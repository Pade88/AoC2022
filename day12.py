def partea_1(my_inputs):
    from collections import deque
    # Facem matricea
    linii = len(my_inputs)
    coloane = len(my_inputs[0])
    C = [[0 for _ in range(coloane)] for _ in range(linii)]
    q = deque() # poti da apendleft() / appendright()
    for lin in range(linii):
        for col in range(coloane):
            if my_inputs[lin][col]=='S':
                C[lin][col] = 1
                # Dau append la indecsi
                q.append(((lin, col), 0))
            elif my_inputs[lin][col] == 'E':
                C[lin][col] = 26
            else:
                C[lin][col] = ord(my_inputs[lin][col])-ord('a')+1

    S = set()
    while q:
        (lin, col), d = q.popleft()
        # Deja verificat
        if (lin, col) in S:
            continue
        # Adaug in set
        S.add((lin, col))
        if my_inputs[lin][col]=='E':
            return d
        for vecin_lin, vecin_col in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = lin + vecin_lin
            cc = col + vecin_col
            # rr si cc cuprinse intre 0 si lin / col
            cond1 = rr >= 0 and rr < linii
            cond2 = cc >= 0 and cc < coloane
            if cond1 and cond2:
                cond3 = C[rr][cc] <= 1 + C[lin][col]
                if cond3:
                    q.append(((rr,cc), d+1))

def partea_2(my_inputs):
    from collections import deque
    # Facem matricea
    linii = len(my_inputs)
    coloane = len(my_inputs[0])
    C = [[0 for _ in range(coloane)] for _ in range(linii)]
    q = deque() # poti da apendleft() / appendright()
    for lin in range(linii):
        for col in range(coloane):
            match my_inputs[lin][col]:
                case 'S':
                    C[lin][col] = 1
                    q.append(((lin, col), 0))
                case 'E':
                    C[lin][col] = 26
                case _:
                    if ord(my_inputs[lin][col])-ord('a') == 0:
                        q.append(((lin, col), 0))
                    C[lin][col] = ord(my_inputs[lin][col])-ord('a')+1

    S = set()
    while q:
        (lin, col), d = q.popleft()
        # Deja verificat
        if (lin, col) not in S:
            S.add((lin, col))
        else: continue
        if my_inputs[lin][col]=='E':
            return d
        # parcurg vecinii
        for vecin_lin, vecin_col in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = lin + vecin_lin
            cc = col + vecin_col
            # rr si cc cuprinse intre 0 si lin / col
            cond1 = rr >= 0 and rr < linii
            cond2 = cc >= 0 and cc < coloane
            if cond1 and cond2:
                cond3 = C[rr][cc] <= 1 + C[lin][col]
                if cond3:
                    q.append(((rr,cc), d+1))

if __name__ == "__main__":
    my_inputs = open("input_day_12.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')