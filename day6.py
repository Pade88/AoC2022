

def partea_1(inputs):
    # Parcurgem sirul
    for idx, char in enumerate(inputs):
        # Pun 4 elemente consecutive intr-un set (contine doar caractere distincte)
        # Daca lungimea setului este 4 (Am gasit 4 caractere distincte consecutive, returnez ultimul index)
        # Folosim list slicing pentru a lua elementele cuprinse intre idx si idx+4
        if len(set(inputs[idx:idx+4])) == 4:
            return (idx + 4)

def partea_2(inputs):
    # Similar, doar ca acum caut 14 caractere consecutive in loc de 4
    for idx, char in enumerate(inputs):
        if len(set(inputs[idx:idx+14])) == 14:
            return (idx + 14)

# UT
print(partea_1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5)
print(partea_1('nppdvjthqldpwncqszvftbrmjlhg') == 6)
print(partea_1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
print(partea_1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)

print(partea_2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19)
print(partea_2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23)
print(partea_2('nppdvjthqldpwncqszvftbrmjlhg') == 23)
print(partea_2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29)
print(partea_2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26)


if __name__ == "__main__":
    my_inputs = open("input_day_6.txt", "r").read()
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')