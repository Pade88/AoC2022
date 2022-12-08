def partea_1(inputs):
    trees = list()
    for tree_line in inputs:
        trees.append([int(tree) for tree in tree_line])

    # Parcurg lista de liste cu pomi, element cu element
    # Ma asigur ca pomul curent este mai mare decat toti pomii de pe aceasi linie si coloana pana la capat
    counter = 0
    for tree_line in range(len(trees)):
        for tree in range(len(trees[tree_line])):
            pom_curent = trees[tree_line][tree]
            # stanga
            if all(trees[tree_line][x] < pom_curent for x in range(tree)):
                counter += 1
                continue
            # dreapta
            if all(trees[tree_line][x] < pom_curent for x in range(tree+1, len(trees[tree_line]))):
                counter += 1
                continue
            # sub
            if all(trees[x][tree] < pom_curent for x in range(tree_line)):
                counter += 1
                continue
            # deasupra
            if all(trees[x][tree] < pom_curent for x in range(tree_line+1, len(trees))):
                counter += 1
                continue
    return counter

def partea_2(inputs):
    trees = list()
    for tree_line in inputs:
        trees.append([int(tree) for tree in tree_line])

    cnt = 0
    for tree_line in range(len(trees)):
        for tree in range(len(trees[tree_line])):
            pom_curent = trees[tree_line][tree]
            # counterele pentru coloane si linii se reseteaza pt fiecare pom
            stanga_cnt = dreapta_cnt = sub_cnt = peste_cnt = 0
            # de la dreapta la stanga (-1, -1)
            for idx_tree in range(tree-1, -1, -1):
                stanga_cnt += 1
                # Opresc iteratia daca exista un pom mai mare decat indexul
                if trees[tree_line][idx_tree] >= pom_curent: break
            # de la stanga la dreapta
            for idx_tree in range(tree+1, len(trees[tree_line])):
                dreapta_cnt += 1
                if trees[tree_line][idx_tree] >= pom_curent: break
            # de jos in sus
            for idx_tree in range(tree_line-1, -1, -1):
                peste_cnt += 1
                if trees[idx_tree][tree] >= pom_curent: break
            # de sus in jos
            for idx_tree in range(tree_line+1, len(trees)):
                sub_cnt += 1
                if trees[idx_tree][tree] >= pom_curent: break
            # Actualizez valoarea maxim
            if stanga_cnt * dreapta_cnt * sub_cnt * peste_cnt > cnt:
                cnt = stanga_cnt * dreapta_cnt * sub_cnt * peste_cnt
    return cnt
# ut
print(partea_1(['30373', '25512', '65332', '33549', '35390']) == 21)
print(partea_2(['30373', '25512', '65332', '33549', '35390']) == 8)

if __name__ == "__main__":
    my_inputs = open("input_day_8.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')