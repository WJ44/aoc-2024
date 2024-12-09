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
        if not i:
            loc += 1
            continue
        size = sizes[-loc]
        if None in ids[:-loc]:
            while size:
                empty_loc = ids.index(None)
                empty_size = sizes[empty_loc]
                if empty_size >= size:
                    ids[-loc] = None
                    sizes[empty_loc] -= size
                    ids.insert(empty_loc, i)
                    sizes.insert(empty_loc, size)
                    size = 0
                else:
                    ids[empty_loc] = i
                    size -= empty_size
        else:
            break

    disk = []
    for i, size in zip(ids, sizes):
        disk.extend([i] * size)

    checksum = 0
    for pos, i in enumerate(disk):
        if i is None:
            break
        checksum += pos * i

    print(checksum)
