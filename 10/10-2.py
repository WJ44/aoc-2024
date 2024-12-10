topo_map = []
trailheads = []
bounds = (0, 0)


def find_score(current_height, pos):
    if current_height == 9:
        return 1
    subtotal = 0
    if pos[1] > 0 and topo_map[pos[1] - 1][pos[0]] == current_height + 1:
        subtotal += find_score(current_height + 1, (pos[0], pos[1] - 1))
    if pos[0] < bounds[0] and topo_map[pos[1]][pos[0] + 1] == current_height + 1:
        subtotal += find_score(current_height + 1, (pos[0] + 1, pos[1]))
    if pos[1] < bounds[1] and topo_map[pos[1] + 1][pos[0]] == current_height + 1:
        subtotal += find_score(current_height + 1, (pos[0], pos[1] + 1))
    if pos[0] > 0 and topo_map[pos[1]][pos[0] - 1] == current_height + 1:
        subtotal += find_score(current_height + 1, (pos[0] - 1, pos[1]))
    return subtotal


with open("./10/input.txt", "r", encoding="utf-8") as file:
    for y, line in enumerate(file):
        row = []
        for x, c in enumerate(line.rstrip()):
            if c == ".":
                height = None
            else:
                height = int(c)
                if height == 0:
                    trailheads.append((x, y))
            row.append(height)
            bounds = (x, y)
        topo_map.append(row)

total = 0
for trailhead in trailheads:
    total += find_score(0, trailhead)

print(total)
