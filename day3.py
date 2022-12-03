my_inputs = open("input_day_3.txt", "r").read().split('\n')

def char_to_int(char):
    if ord(char) > 64 and ord(char) <  91:
        return ord(char) - 38
    else:
        return ord(char) - 96

global_sum = 0
for item in my_inputs:
    comp1_set = set()
    comp2_set = set()
    item_sum = 0
    # Impartim stringul in 2 componente egale
    comp1, comp2 = item[:int(len(item)/2)], item[int(len(item)/2):]
    # Punem fiecare element din string intr-un set
    for sub_item_1, sub_item_2 in zip(comp1, comp2):
        comp1_set.add(sub_item_1)
        comp2_set.add(sub_item_2)
    # Intersectam caractele din stanga cu cele din dreapta
    # Elementele comune sunt convertite la numeric si adunate
    for common_item in comp1_set.intersection(comp2_set):
        item_sum += char_to_int(common_item)
    global_sum += item_sum
print(f'Solutia partea 1: {global_sum}')

sum = 0
# spargem lista in subliste de 3
for item in range(0, len(my_inputs), 3):
    chunk = my_inputs[item:item+3]
    # fiecare element e convertit la set, apoi facem intersectia intre ele
    tmp = set(chunk[0]).intersection(set(chunk[1]))
    common_item = tmp.intersection(set(chunk[2]))
    # Elementul comun dupa intersectie e convertit la prioritate si adunat
    for new_item in common_item:
        sum += char_to_int(new_item)
print(f'Solutia partea 2: {sum}')











# def ut(item):
#     comp1_set = set()
#     comp2_set = set()
#     sum = 0
#     comp1, comp2 = item[:int(len(item)/2)], item[int(len(item)/2):]
#     for sub_item_1, sub_item_2 in zip(comp1, comp2):
#         comp1_set.add(sub_item_1)
#         comp2_set.add(sub_item_2)
#     for common_item in comp1_set.intersection(comp2_set):
#         sum += char_to_int(common_item)

# ut('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')