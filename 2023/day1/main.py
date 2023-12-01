def first(filename):
    total = 0
    with open(filename) as file:
        while line:=file.readline():
            for char in line:
                if char.isnumeric():
                      first = char
                      break
            for char in line[::-1]:
                if char.isnumeric():
                    last = char
                    break
            total += int(first+last)
    return total

def second(filename):
    total = 0
    digits = [chr(i) for i in range(48, 58)] + ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = {
        "zero": "0", "0": "0",
        "one": "1", "1": "1",
        "two": "2", "2": "2",
        "three": "3",  "3": "3",
        "four": "4", "4": "4",
        "five": "5", "5": "5",
        "six": "6", "6": "6",
        "seven": "7", "7": "7",
        "eight": "8", "8": "8",
        "nine": "9", "9": "9"
    }
    with open(filename) as file:
        while line:=file.readline():
            strings = [[line[start:start+size] for size in (1, 3, 4, 5)] for start in range(len(line))]
            # Find first number
            for start_pos in strings:
                for attempt in start_pos:
                    if attempt in digits:
                        first = attempt
                        break
                else: continue
                break

            # Find last number
            for start_pos in strings[::-1]:
                for attempt in start_pos:
                    if attempt in digits:
                        last = attempt
                        break
                else: continue
                break

            total += int(numbers[first]+numbers[last])
    return total

print(f"First answer: {first('input.txt')}")
print(f"Second answer: {second('input.txt')}")