import re

def text_parser(my_inputs: list) -> tuple:
    # Parseaza textul cu stackurile
    txt_stackuri, instructiuni = my_inputs
    stack = list()
    instr = list()
    lines = txt_stackuri.split("\n")[:-1]
    # parcurgem textul, si punem fiecare element intr-o lista, cu justify left de 10 (pentru a scapa de spatiile dintre caractere)
    for idx, line in enumerate(zip(*map(lambda x: list(x.ljust(10)), lines))):
        # if idx % 3 == 0 nu merge, linia cu numarul stackurilor incepe cu spatiu (IQ 200 :| )
        # Parcurgem pe latime, si punem fiecare coloana inversata (citita de jos in sus) in stack
        if idx % 4 == 1:
            stack.append("".join(reversed(line)).strip())

    # parsez instructiunile, si cu un regex, extragem doar numarul de crates, sursa si destinatia
    for instructiune in instructiuni.strip().split('\n'):
        # Eg: move 7 from 3 to 9 -> (7, 3, 9)
        quant, from_, to_ = re.findall(r"\d+", instructiune)
        # Convertim la int
        quant, from_, to_ = int(quant), int(from_), int(to_)
        instr.append((quant, from_, to_))
    return stack, instr

def partea_1(my_inputs: list) -> str:
    stack, instructiuni = text_parser(my_inputs)
    stack = [ None ] + stack[:]
    for cant, de_la, pana_la in instructiuni:
        # Selecteaza ultima cant cutii din varful stivei sursa
        cutie = stack[de_la][-cant:][::-1]
        # Adauga cutia in varful stivei destinatie
        stack[pana_la] = stack[pana_la] + cutie
        # Sterge cutiile din stiva sursa
        stack[de_la] = stack[de_la][:-cant]
    # returneaza stivele inversate (de jos in sus)
    return "".join(stack_[-1] for stack_ in stack[1:])



def partea_2(my_inputs: list) -> str:
    stack, instructiuni = text_parser(my_inputs)
    stack = [ None ] + stack[:]
    for cant, de_la, pana_la in instructiuni:
        # Selecteaza ultima cant cutii din varful stivei sursa
        cutie = stack[de_la][-cant:][::-1]
        # Pentru partea 2 doar inversez ordinea cutiilor selectate (pastrez logica naturala)
        cutie = cutie[::-1]
        # Adauga cutia in varful stivei destinatie
        stack[pana_la] = stack[pana_la] + cutie
        # Sterge cutiile din stiva sursa
        stack[de_la] = stack[de_la][:-cant]
    # returneaza stivele inversate (de jos in sus)
    return "".join(stack_[-1] for stack_ in stack[1:])

# teste
txt_part_1 = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\n'\
'move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'
print(partea_1(txt_part_1.split("\n\n")) == 'CMZ')
print(partea_2(txt_part_1.split("\n\n")) == 'MCD')

if __name__ == '__main__':
    my_inputs = open("input_day_5.txt", "r").read().split('\n\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')