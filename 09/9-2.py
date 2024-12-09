with open("./09/input.txt", "r", encoding="utf-8") as file:
    disk_map = [int(c) for c in file.read()]
    ids = []
    sizes = []
    empty = False
    i = 0
    for size in disk_map:
        if empty:
            ids.append(None)
            sizes.append(size)
            empty = False
        else:
            ids.append(i)
            sizes.append(size)
            i += 1
            empty = True

    loc = 1
    while loc <= len(ids):
        i = ids[-loc]
        if i is None:
            loc += 1
            continue
        size = sizes[-loc]
        for empty_loc, empty_size in enumerate(sizes[:-loc]):
            if ids[empty_loc] is None and empty_size >= size:
                ids[-loc] = None
                sizes[empty_loc] -= size
                ids.insert(empty_loc, i)
                sizes.insert(empty_loc, size)
                break
        loc += 1

    disk = []
    for i, size in zip(ids, sizes):
        disk.extend([i] * size)

    checksum = 0
    for pos, i in enumerate(disk):
        if i is None:
            continue
        checksum += pos * i

    print(checksum)
