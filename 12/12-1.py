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
for plots in plants.values():
    while plots:
        region = add_neighbours(plots.pop(), set())
        regions.append(region)
        plots -= region

total = 0
for region in regions:
    area = 0
    perimiter = 0
    for plot in region:
        p = 4
        if (plot[0] - 1, plot[1]) in region:
            p -= 1
        if (plot[0], plot[1] + 1) in region:
            p -= 1
        if (plot[0] + 1, plot[1]) in region:
            p -= 1
        if (plot[0], plot[1] - 1) in region:
            p -= 1
        area += 1
        perimiter += p
    total += area * perimiter

print(total)
