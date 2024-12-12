plants = {}

with open("./12/input.txt", "r", encoding="utf-8") as file:
    garden = [list(line.rstrip()) for line in file]

    bounds = (len(garden[0]), len(garden))

    for y, row in enumerate(garden):
        for x, plot in enumerate(row):
            if plot not in plants:
                plants[plot] = set()
            plants[plot].add((x, y))


def add_neighbours(location, current_region):
    current_region.add(location)
    if (neigbour := (location[0] - 1, location[1])) in plots and neigbour not in current_region:
        current_region.add(neigbour)
        add_neighbours(neigbour, current_region)
    if (neigbour := (location[0], location[1] + 1)) in plots and neigbour not in current_region:
        current_region.add(neigbour)
        add_neighbours(neigbour, current_region)
    if (neigbour := (location[0] + 1, location[1])) in plots and neigbour not in current_region:
        current_region.add(neigbour)
        add_neighbours(neigbour, current_region)
    if (neigbour := (location[0], location[1] - 1)) in plots and neigbour not in current_region:
        current_region.add(neigbour)
        add_neighbours(neigbour, current_region)
    return current_region


regions = []
for plant, plots in plants.items():
    while plots:
        region = add_neighbours(plots.pop(), set())
        regions.append((region, plant))
        plots -= region

total = 0
for region, plant in regions:
    sides = 0
    visited = set()
    for plot in region:
        for v in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            current = plot
            start = (current, v)
            current_side = None
            first_side = None
            if start not in visited:
                while True:
                    visited.add((current, v))
                    if (new := (current[0] + v[0], current[1] + v[1])) not in region:
                        if v != current_side:
                            sides += 1
                            current_side = v
                            if not first_side:
                                first_side = current_side
                        v = (v[1] * -1, v[0])
                    else:
                        current = new
                        v = (v[1], v[0] * -1)
                    if (current, v) == start:
                        if current_side and current_side == first_side:
                            sides -= 1
                        break
    total += sides * len(region)
print(total)
