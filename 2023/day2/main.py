def parse_line(line):
    game_id, rounds = line.strip().split(":")
    game_id = int(game_id.split()[-1])
    rounds = rounds.split(";")
    
    values = [{} for _ in range(len(rounds))]
    for i, round in enumerate(rounds):
        for color in round.split(','):
            ammount, name = color.strip().split()
            values[i][name] = int(ammount)

    return game_id, values

def first(filename):
    total = 0
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open(filename) as file:
        for line in file.readlines():
            game_id, rounds = parse_line(line)
            if all([bag[value] >= round[value] for round in rounds for value in round]):
                total += game_id
    
    return total

def second(filename):
    total = 0
    with open(filename) as file:
        for line in file.readlines():
            subtotal = 1
            game_id, rounds = parse_line(line)
            
            min_values = dict(
                [(value, max(round[value] if value in round else 1 for round in rounds)) for value in ["blue", "red", "green"]]
            )
            for value in min_values:
                subtotal *= min_values[value]
            total += subtotal
    return total


print(f"First answer: {first('input.txt')}")
print(f"Second answer: {second('input.txt')}")