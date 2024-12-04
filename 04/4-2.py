rows = []
with open("./04/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        rows.append(line.rstrip())

count = 0
for y in range(len(rows) - 2):
    for x in range(len(rows[0]) - 2):
        diag1 = "" + rows[y][x] + rows[y + 1][x + 1] + rows[y + 2][x + 2]
        diag2 = "" + rows[y + 2][x] + rows[y + 1][x + 1] + rows[y][x + 2]

        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            count += 1

print(count)
