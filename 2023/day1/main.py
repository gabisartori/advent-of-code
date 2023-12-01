def first(filename):
    total = 0
    with open(filename) as file:
        while line:=file.readline():
            found_first = False
            first = last = None
            for char in line:
                if char.isnumeric():
                    last = char
                    if not found_first:
                        first = char
                        found_first = True
            total += int(first+last)
    return total

def second(filename):
    total = 0
    output = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = {
        "zero": "0",
        "0": "0",
        "one": "1",
        "1": "1",
        "two": "2",
        "2": "2",
        "three": "3",
        "3": "3",
        "four": "4",
        "4": "4",
        "five": "5",
        "5": "5",
        "six": "6",
        "6": "6",
        "seven": "7",
        "7": "7",
        "eight": "8",
        "8": "8",
        "nine": "9",
        "9": "9"
    }
    with open(filename) as file:
        while line:=file.readline():
            found_first = False
            strings = [[line[start:start+size] for size in (1, 3, 4, 5)] for start in range(len(line))]
            for start_pos in strings:
                for attempt in start_pos:
                    if attempt in digits:
                        last = attempt
                        if not found_first:
                            first = attempt
                            found_first = True
            output.append(first+last)
            total += int(numbers[first] + numbers[last])
    return total

print(second('input.txt'))
