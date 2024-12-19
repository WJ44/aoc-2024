robots = []

seconds = 100

bounds = (101, 103)

with open("./14/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        p, v = line.split()
        p = p[2:].split(",")
        v = v[2:].split(",")
        robots.append((int(p[0]), int(p[1]), int(v[0]), int(v[1])))

quadrants = [0, 0, 0, 0]
for p_x, p_y, v_x, v_y in robots:
    x = (p_x + v_x * seconds) % bounds[0]
    y = (p_y + v_y * seconds) % bounds[1]

    if x < bounds[0] // 2 and y < bounds[1] // 2:
        quadrants[0] += 1
    elif x > bounds[0] // 2 and y < bounds[1] // 2:
        quadrants[1] += 1
    elif x < bounds[0] // 2 and y > bounds[1] // 2:
        quadrants[2] += 1
    elif x > bounds[0] // 2 and y > bounds[1] // 2:
        quadrants[3] += 1

total = 1
for q in quadrants:
    total *= q

print(total)
