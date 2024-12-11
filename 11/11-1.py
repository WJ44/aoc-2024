blinks = 25

with open("./11/input.txt", "r", encoding="utf-8") as file:
    stones = [int(x) for x in file.read().split()]

    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            stone_str = str(stone)
            stone_len = len(stone_str)
            if stone == 0:
                new_stones.append(1)
            elif stone_len % 2 == 0:
                new_stones.append(int(stone_str[: stone_len // 2]))
                new_stones.append(int(stone_str[stone_len // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))
