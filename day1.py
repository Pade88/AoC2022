my_inputs = open("Python/AOC2022/input_day_1.txt", "r").read().split('\n')
# Part 1
max_kcal = 0
current_kcal_sum = 0

for kcal in my_inputs:
    if kcal != '':
        current_kcal_sum += int(kcal)
    else:
        # Verifica daca maximul a fost depasit
        # Reseteaza contorul
        if current_kcal_sum > max_kcal:
            max_kcal = current_kcal_sum
        current_kcal_sum = 0

print(f'Solutia partea 1: {max_kcal}')

# Part 2
kcal_per_elf = set()
current_kcal_sum = 0
for kcal in my_inputs:
    if kcal != '':
        current_kcal_sum += int(kcal)
    else:
        # Adauga suma de calorii in set, reseteaza contorul
        kcal_per_elf.add(current_kcal_sum)
        current_kcal_sum = 0
# Selecteaza cele mai mari 3 valori din set-ul sortat (-3:)
top3_kcal = (sorted(kcal_per_elf)[-3:])

print(f'Solutia partea 2: {sum(top3_kcal)}')