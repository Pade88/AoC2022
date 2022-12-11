class monkey:
    def __init__(self, id, _iteme, op, test, test_tru, test_fals):
        self.id = id
        self.items = _iteme
        self.op = op
        self.test = test
        self.test_tru = test_tru
        self.test_fals = test_fals

def create_monkeys(my_inputs):
    monkeys = list()
    for line in my_inputs:
        if not line:
            # instantiaza obj
            monkeys.append(monkey(monkey_id, items, op, tst, if_true, if_false))
            continue
        match line.strip().split()[0]:
            case 'Monkey':
                monkey_id = int(line.split()[-1].replace(':', ''))
            case 'Starting':
                items = line.strip().split('Starting items: ')[1:]
                items = list(map(int, items[0].split(', ')))
            case 'Operation:':
                op = line.strip().split('Operation:')[-1]
                # String la functie
                op = eval("lambda old:" + line.split("=")[1])
            case 'Test:':
                print(line)
                tst = int(line.strip().split('divisible by')[-1])
                print(tst)
            case 'if':
                print(line)
                if_true = line.strip().split('if true:')[-1]
                print(if_true)
            case 'if false:':
                if_false = line.strip().split('if false:')[-1]
            case _:
                if 'true' in line:
                    # Stochez doar monkey id
                    if_true = int(line.strip().split()[-1])
                else:
                    if_false = int(line.strip().split()[-1])
    return monkeys

def partea_1(my_inputs):
    monkeys = create_monkeys(my_inputs)
    counter = [0] * len(monkeys)
    for _ in range(20):
        for idx, monkey in enumerate(monkeys):
            for item in monkey.items:
                # Pentru fiecare item, aplic fct lambda si impart la 3
                item = monkey.op(item)
                item //= 3
                if item % monkey.test == 0:
                    monkeys[monkey.test_tru].items.append(item)
                else:
                    monkeys[monkey.test_fals].items.append(item)
            counter[idx] += len(monkey.items)
            monkey.items = []
    
    counter.sort()
    return (counter[-1] * counter[-2])

def partea_2(my_inputs):
    monkeys = create_monkeys(my_inputs)
    counter = [0] * len(monkeys)
    for _ in range(10_000):
        for idx, monkey in enumerate(monkeys):
            for item in monkey.items:
                # Pentru fiecare item, aplic fct lambda si impart la 3
                item = monkey.op(item)
                item //= 3
                if item % monkey.test == 0:
                    monkeys[monkey.test_tru].items.append(item)
                else:
                    monkeys[monkey.test_fals].items.append(item)
            counter[idx] += len(monkey.items)
            monkey.items = []
    
    counter.sort()
    return (counter[-1] * counter[-2])

if __name__ == "__main__":
    my_inputs = open("input_day_11.txt", "r").read().split('\n')
    print(f'Solutia partea 1: {partea_1(my_inputs)}')
    print(f'Solutia partea 2: {partea_2(my_inputs)}')