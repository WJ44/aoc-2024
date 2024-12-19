move_mapping = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

walls = set()
boxes = set()
robot = (0, 0)
moves = []


def can_move(m):
    i = 1
    while (loc := (robot[0] + i * m[0], robot[1] + i * m[1])) not in walls:
        if loc not in boxes:
            return loc
        i += 1
    return False


with open("./15/input.txt", "r", encoding="utf-8") as file:
    warehouse, movements = file.read().split("\n\n")
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x, y))
            elif c == "O":
                boxes.add((x, y))
            elif c == "@":
                robot = (x, y)
    for c in movements.replace("\n", ""):
        moves.append(move_mapping[c])

for move in moves:
    pos = (robot[0] + move[0], robot[1] + move[1])
    if hole := can_move(move):
        if pos != hole:
            boxes.remove(pos)
            boxes.add(hole)
        robot = pos

total = 0
for x, y in boxes:
    total += 100 * y + x

print(total)
