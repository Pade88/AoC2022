import re
regex = r"^Valve ([A-Z]{2}) has flow rate=(\d*); tunnels? leads? to valves? (([A-Z]{2})(, [A-Z]{2})*)$"
def partea_1(my_inputs):
    valves = dict()
    for valve, flowrate, tunnels, *_ in map(lambda x: re.fullmatch(regex, x).groups(), my_inputs):
        valves.update({valve: (int(flowrate), tunnels.split(", "))})
    # valves contine numele valvei, debitul, si urmatoarele destinatii
    def inner(sec=30-1, pos='AA', status=dict(), vizitat = dict()):
        # Comprehension, ca sa am un sum gol cel putin
        #for k, v in status.items():
        #    if v is not None:
        #       q = sum(v * valves[k][0])
        q = sum(v * valves[k][0] for k, v in status.items() if v is not None)
        # Sec ajunge la 0
        if not sec:
            return q
        # daca secunda si pozitia sunt deja vizitate, iesim din recursiune
        if vizitat.get((sec, pos), -1) >= q:
            return 0
        vizitat[sec, pos] = q
        
        # Rulam toate miscarile
        m = 0
        for p0 in [ pos ] + valves[pos][1]:
            if pos == p0:
                # Memorez pozitia si secunda daca exista
                if status.get(pos) is None and valves[pos][0] > 0:
                    status[pos] = sec
                else:
                    continue
                    
            # ma duc la urmatoarea valva rec
            m = max(m, inner(sec - 1, p0, status, vizitat))
            
            if pos == p0:
                status[pos] = None
        
        return m
    return inner()

def partea_2(my_inputs):
    pass

if __name__ == "__main__":
    my_inputs = open("input_day_16.txt", "r").read().strip().split("\n")
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')