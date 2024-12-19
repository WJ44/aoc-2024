from time import sleep

positions = []
velocities = []

bounds = (101, 103)

with open("./14/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        p, v = line.split()
        p = p[2:].split(",")
        v = v[2:].split(",")
        positions.append((int(p[0]), int(p[1])))
        velocities.append((int(v[0]), int(v[1])))


def tree():
    robots = sorted(list(set(positions)), key=lambda x: x[1])
    top = robots.pop(0)
    while robots:
        robot1 = robots.pop(0)
        if robot1[0] == top[0]:
            continue
        if not robots:
            return False
        if (robot2 := (top[0] + top[0] - robot1[0], robot1[1])) in robots:
            robots.remove(robot2)
        else:
            return False
    return True


def display():
    picture = [["." for x in range(bounds[0])] for y in range(bounds[1])]
    for x, y in positions:
        picture[y][x] = "O"
    for x in ["".join(y) for y in picture]:
        print(x)
    print("-------------")
    print(seconds)
    sleep(0.1)


seconds = 0
while not tree():
    for i, p in enumerate(positions):
        positions[i] = ((p[0] + velocities[i][0]) % bounds[0], (p[1] + velocities[i][1]) % bounds[1])
    seconds += 1
    if (seconds - 99) % 101 == 0:
        display()
    # print(seconds)


print(seconds)
