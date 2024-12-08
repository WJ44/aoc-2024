from itertools import combinations

antennas = {}
bounds = (0, 0)

with open("./08/input.txt", "r", encoding="utf-8") as file:
    for y, line in enumerate(file):
        for x, tile in enumerate(line.rstrip()):
            if tile != ".":
                if not tile in antennas:
                    antennas[tile] = []
                antennas[tile].append((x, y))
            bounds = (x, y)

antinodes = set()
for frequency, locations in antennas.items():
    for loc1, loc2 in combinations(locations, 2):
        antinode = (loc1[0] + 2 / 3 * (loc2[0] - loc1[0]), loc1[1] + 2 / 3 * (loc2[1] - loc1[1]))
        if (
            int(antinode[0]) == antinode[0]
            and int(antinode[1]) == antinode[1]
            and 0 <= antinode[0] <= bounds[0]
            and 0 <= antinode[1] <= bounds[1]
        ):
            antinodes.add(antinode)
        antinode = (loc2[0] - 2 / 3 * (loc2[0] - loc1[0]), loc2[1] - 2 / 3 * (loc2[1] - loc1[1]))
        if (
            int(antinode[0]) == antinode[0]
            and int(antinode[1]) == antinode[1]
            and 0 <= antinode[0] <= bounds[0]
            and 0 <= antinode[1] <= bounds[1]
        ):
            antinodes.add(antinode)
        antinode = (loc1[0] + 2 * (loc2[0] - loc1[0]), loc1[1] + 2 * (loc2[1] - loc1[1]))
        if (
            int(antinode[0]) == antinode[0]
            and int(antinode[1]) == antinode[1]
            and 0 <= antinode[0] <= bounds[0]
            and 0 <= antinode[1] <= bounds[1]
        ):
            antinodes.add(antinode)
        antinode = (loc2[0] - 2 * (loc2[0] - loc1[0]), loc2[1] - 2 * (loc2[1] - loc1[1]))
        if (
            int(antinode[0]) == antinode[0]
            and int(antinode[1]) == antinode[1]
            and 0 <= antinode[0] <= bounds[0]
            and 0 <= antinode[1] <= bounds[1]
        ):
            antinodes.add(antinode)

print(len(antinodes))
