rows = []
with open("./04/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        rows.append(line.rstrip())

if len(rows) > len(rows[0]):
    padding = " " * (len(rows) - len(rows[0]))
    for row in rows:
        row += padding
else:
    padding = " " * len(rows[0])
    for _ in range(len(rows[0]) - len(rows)):
        rows.append(padding)

columns = ["".join(row[i] for row in rows) for i in range(len(rows[0]))]

test = rows.copy()
diagonals = []
for start_y, _ in enumerate(rows):
    x = 0
    y = start_y
    diagonal = ""
    while 0 <= y < len(rows) and 0 <= x < len(columns):
        diagonal += rows[y][x]
        x += 1
        y += 1
    diagonals.append(diagonal)
    x = 0
    y = start_y
    diagonal = ""
    while 0 <= y < len(rows) and 0 <= x < len(columns):
        diagonal += rows[y][x]
        x += 1
        y += -1
    diagonals.append(diagonal)

for start_x in range(1, len(rows[0])):
    x = start_x
    y = 0
    diagonal = ""
    while 0 <= y < len(rows) and 0 <= x < len(columns):
        diagonal += rows[y][x]
        x += 1
        y += 1
    diagonals.append(diagonal)
    x = start_x
    y = len(rows) - 1
    diagonal = ""
    while 0 <= y < len(rows) and 0 <= x < len(columns):
        diagonal += rows[y][x]
        x += 1
        y += -1
    diagonals.append(diagonal)

lines = rows + columns + diagonals

count = 0
for line in lines:
    count += line.count("XMAS")
    count += line.count("SAMX")

print(count)
