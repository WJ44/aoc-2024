move_mapping = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

walls = set()
boxes = set()
robot = (0, 0)
moves = []


def can_move(m):
    to_move = set()
    free = None
    if m == (1, 0):
        i = 1
        while (loc := (robot[0] + i, robot[1])) not in walls:
            if loc in boxes:
                to_move.add(loc)
            elif loc not in boxes and (robot[0] + i - 1, robot[1]) not in boxes:
                free = loc
                break
            i += 1
    elif m == (-1, 0):
        i = 1
        while (loc := (robot[0] - i - 1, robot[1])) not in walls:
            if loc in boxes:
                to_move.add(loc)
            elif loc not in boxes and (loc2 := (robot[0] - i, robot[1])) not in boxes:
                free = loc2
                break
            i += 1
    elif m in [(0, 1), (0, -1)]:
        row = {(robot[0], robot[1] + m[1])}
        while not any(box in walls or (box[0] - 1, box[1]) in walls for box in row):
            new_row = set()
            for box in row:
                if box in boxes:
                    to_move.add(box)
                    new_row.add((box[0], box[1] + m[1]))
                    new_row.add((box[0] + 1, box[1] + m[1]))
                elif (box2 := (box[0] - 1, box[1])) in boxes:
                    to_move.add(box2)
                    new_row.add((box[0] - 1, box[1] + m[1]))
                    new_row.add((box[0], box[1] + m[1]))
            if not new_row:
                free = row
                break
            row = new_row
    if not free:
        return False

    boxes.difference_update(to_move)
    for box in to_move:
        boxes.add((box[0] + m[0], box[1] + m[1]))
    return True


with open("./15/input.txt", "r", encoding="utf-8") as file:
    warehouse, movements = file.read().split("\n\n")
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((2 * x, y))
            elif c == "O":
                boxes.add((2 * x, y))
            elif c == "@":
                robot = (2 * x, y)
    for c in movements.replace("\n", ""):
        moves.append(move_mapping[c])

for move in moves:
    pos = (robot[0] + move[0], robot[1] + move[1])
    if hole := can_move(move):
        robot = pos

total = 0
for x, y in boxes:
    total += 100 * y + x

print(total)
