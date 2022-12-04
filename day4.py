my_inputs = open("input_day_4.txt", "r").read().split('\n')

cnt = 0
for parse in my_inputs:
    elf_1_section, elf_2_section = parse.split(",")
    elf1_1_start, elf_1_stop = elf_1_section.split("-")
    elf1_2_start, elf_2_stop = elf_2_section.split("-")
    range_elf_1 =  set(range(int(elf1_1_start), int(elf_1_stop) + 1))
    range_elf_2 =  set(range(int(elf1_2_start), int(elf_2_stop) + 1))
    # daca range-ul 1 este subset range-ului 2 si invers
    if range_elf_2.issubset(range_elf_1) or range_elf_1.issubset(range_elf_2):
        cnt += 1
print(f'Solutia partea 1: {cnt}')

cnt2 = 0
for parse in my_inputs:
    elf_1_section, elf_2_section = parse.split(",")
    elf1_1_start, elf_1_stop = elf_1_section.split("-")
    elf1_2_start, elf_2_stop = elf_2_section.split("-")
    range_elf_1 =  set(range(int(elf1_1_start), int(elf_1_stop) + 1))
    range_elf_2 =  set(range(int(elf1_2_start), int(elf_2_stop) + 1))
    # contorizeaza daca exista suprapuneri
    if range_elf_1.intersection(range_elf_2):
        cnt2 += 1
print(f'Solutia partea 2: {cnt2}')