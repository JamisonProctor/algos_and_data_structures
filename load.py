def load_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))

    return numbers