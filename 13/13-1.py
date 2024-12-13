import re

machines = []

with open("./13/input.txt", "r", encoding="utf-8") as file:
    for machine in file.read().split("\n\n"):
        m = re.match(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", machine)
        machines.append((m.group(1, 2), m.group(3, 4), m.group(5, 6)))

total = 0
for A, B, prize in machines:
    A = (int(A[0]), int(A[1]))
    B = (int(B[0]), int(B[1]))
    prize = (int(prize[0]), int(prize[1]))
    minimum = None
    for a in range(101):
        if (
            (prize[0] - a * A[0]) % B[0] != 0
            or (prize[1] - a * A[1]) % B[1] != 0
            or (prize[0] - a * A[0]) // B[0] != (prize[1] - a * A[1]) // B[1]
            or not 0 <= (prize[0] - a * A[0]) // B[0] <= 100
        ):
            continue
        if not minimum or a * 3 + (prize[0] - a * A[0]) // B[0] < minimum:
            minimum = a * 3 + (prize[0] - a * A[0]) // B[0]
    if minimum:
        total += minimum

print(total)
