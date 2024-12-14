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
    prize = (int(prize[0]) + 10000000000000, int(prize[1]) + 10000000000000)

    b = (A[0] * prize[1] - A[1] * prize[0]) / (A[0] * B[1] - A[1] * B[0])
    a = (prize[0] - b * B[0]) / A[0]

    if a == int(a) and b == int(b):
        total += int(a * 3 + b)

print(total)
