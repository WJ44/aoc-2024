stones = {}
blinks = 75

with open("./11/input.txt", "r", encoding="utf-8") as file:
    for stone in file.read().split():
        stone = int(stone)
        if stone not in stones:
            stones[stone] = 1
        else:
            stones[stone] += 1

    for blink in range(blinks):
        for stone, count in stones.copy().items():
            stones[stone] -= count
            if stone == 0:
                if 1 not in stones:
                    stones[1] = 0
                stones[1] += count
            elif (stone_len := len(stone_str := str(stone))) % 2 == 0:
                if (first := int(stone_str[: stone_len // 2])) not in stones:
                    stones[first] = 0
                if (second := int(stone_str[stone_len // 2 :])) not in stones:
                    stones[second] = 0
                stones[first] += count
                stones[second] += count
            else:
                if (new := stone * 2024) not in stones:
                    stones[new] = 0
                stones[stone * 2024] += count

    print(sum(stones.values()))
