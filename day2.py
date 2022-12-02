my_inputs = open("input_day_2.txt", "r").read().split('\n')

# Puncte const
LOSS = 0
DRAW = 3
WIN = 6
ROCK = 1
PAPPER = 2
SCRISSORS = 3

sum = 0
for round in my_inputs:
    score = 0
    oponent, me = round.split(" ")
    match oponent:
        case "A": # Rock
            if me == "X": # Rock
                score = ROCK + DRAW
            elif me == "Y": # Papper
                score = PAPPER + WIN
            else: # Scrissor
                score = SCRISSORS + LOSS
        case "B": # papper
            if me == "X": # Rock
                score = ROCK + LOSS
            elif me == "Y": # Papper
                score = PAPPER + DRAW
            else: # Scrissor
                score = SCRISSORS + WIN
        case "C": # Scrissor
            if me == "X": # Rock
                score = ROCK + WIN
            elif me == "Y": # Papper
                score = PAPPER + LOSS
            else: # Scrissor
                score = SCRISSORS + DRAW
    sum += score
print(f'Solutia partea 1: {sum}')

# part 2
sum = 0
for round in my_inputs:
    score = 0
    oponent, me = round.split(" ")
    match oponent:
        case "A": # Rock
            if me == "X": # Scris
                score = SCRISSORS + LOSS
            elif me == "Y": # Rock
                score = ROCK + DRAW
            else: # Papper
                score = PAPPER + WIN
        case "B": # Papper
            if me == "X": # Lose
                score = ROCK + LOSS
            elif me == "Y": # Draw
                score = PAPPER + DRAW
            else: # Win
                score = SCRISSORS + WIN
        case "C": # Scrissor
            if me == "X": # Lose
                score = PAPPER + LOSS
            elif me == "Y": # Draw
                score = SCRISSORS + DRAW
            else: # Win
                score = ROCK + WIN
    sum += score

print(f'Solutia partea 2: {sum}')

# hash

reguli = {
    "A X": DRAW + ROCK, # Rock - Rock
    "A Y": WIN + PAPPER, # Rock - Papper
    "A Z": LOSS + SCRISSORS, # Rock - Scrissor
    "B X": LOSS + ROCK, # Papper - Rock
    "B Y": DRAW + PAPPER, # Papper- Papper
    "B Z": WIN + SCRISSORS, # Papper - Scrissor
    "C X": WIN + ROCK, # Scrissor - rock
    "C Y": LOSS + PAPPER, # Scrissor - paper
    "C Z": DRAW + SCRISSORS, # Scrissor - scrissor
}
sum = 0
for round in my_inputs:
    sum += reguli[round]
print(f'Solutia partea 1: {sum}')

# part2
reguli = {
    "A X": LOSS + SCRISSORS, # Rock - Rock
    "A Y": DRAW + ROCK, # Rock - Papper
    "A Z": WIN + PAPPER, # Rock - Scrissor
    "B X": LOSS + ROCK, # Papper - Rock
    "B Y": DRAW + PAPPER, # Papper- Papper
    "B Z": WIN + SCRISSORS, # Papper - Scrissor
    "C X": LOSS + PAPPER, # Scrissor - rock
    "C Y": DRAW + SCRISSORS, # Scrissor - paper
    "C Z": WIN + ROCK, # Scrissor - scrissor
}
sum = 0
for round in my_inputs:
    sum += reguli[round]
print(f'Solutia partea 2: {sum}')