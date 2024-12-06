with open("./06/input.txt", "r", encoding="utf-8") as file:
    grid = [list(row.rstrip()) for row in file]

    guard_start = None
    for r, row in enumerate(grid):
        if "^" in row:
            guard_start = ((r, row.index("^")), (-1, 0))
        elif "v" in row:
            guard_start = ((r, row.index("v")), (1, 0))
        elif "<" in row:
            guard_start = ((r, row.index("<")), (0, -1))
        elif ">" in row:
            guard_start = ((r, row.index(">")), (0, 1))

    visited = set()
    guard = guard_start
    while True:
        visited.add(guard[0])
        next_pos = (guard[0][0] + guard[1][0], guard[0][1] + guard[1][1])
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[next_pos[0]])):
            break
        next_tile = grid[next_pos[0]][next_pos[1]]
        if next_tile == "#":
            guard = (guard[0], (guard[1][1], guard[1][0] * -1))
        else:
            guard = (next_pos, guard[1])

    obstacles = []
    for r, c in visited:
        if grid[r][c] != ".":
            continue
        visited_new = []
        grid_new = [row.copy() for row in grid]
        grid_new[r][c] = "#"
        guard = guard_start
        while True:
            if guard in visited_new:
                obstacles.append((r, c))
                break
            visited_new.append(guard)
            next_pos = (guard[0][0] + guard[1][0], guard[0][1] + guard[1][1])
            if not (0 <= next_pos[0] < len(grid_new) and 0 <= next_pos[1] < len(grid_new[next_pos[0]])):
                break
            next_tile = grid_new[next_pos[0]][next_pos[1]]
            if next_tile == "#":
                guard = (guard[0], (guard[1][1], guard[1][0] * -1))
            else:
                guard = (next_pos, guard[1])

    print(len(obstacles))
