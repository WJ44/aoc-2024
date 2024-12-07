equations = []

with open("./07/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip()
        line = line.split(":")
        equations.append((int(line[0]), [int(x) for x in line[1].split()]))


def test_possibilities(current, remaining):
    if not remaining:
        return [current]
    answers = []
    answers.extend(test_possibilities(current * remaining[0], remaining[1:]))
    answers.extend(test_possibilities(current + remaining[0], remaining[1:]))
    return answers


total = 0
for test_value, numbers in equations:
    if test_value in test_possibilities(numbers[0], numbers[1:]):
        total += test_value

print(total)
