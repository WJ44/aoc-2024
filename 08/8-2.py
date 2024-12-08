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
        antinodes.update(
            [
                (loc1[0] + x * (loc2[0] - loc1[0]), loc1[1] + x * (loc2[1] - loc1[1]))
                for x in range(-bounds[0], bounds[0])
                if 0 <= loc1[0] + x * (loc2[0] - loc1[0]) <= bounds[0]
                and 0 <= loc1[1] + x * (loc2[1] - loc1[1]) <= bounds[1]
            ]
        )

print(len(antinodes))
