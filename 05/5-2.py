incorrect = []

with open("./05/input.txt", "r", encoding="utf-8") as file:
    rules, updates = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rules.splitlines()]
    rules = [(int(X), int(Y)) for X, Y in rules]

    updates = [[int(x) for x in update.split(",")] for update in updates.splitlines()]

    for update in updates:
        for X, Y in rules:
            if X in update and Y in update and update.index(X) > update.index(Y):
                incorrect.append(update)
                break


total = 0
for update in incorrect:
    changed = True
    while changed:
        changed = False
        for X, Y in rules:
            if X in update and Y in update:
                i_X = update.index(X)
                i_Y = update.index(Y)
                if i_X > i_Y:
                    update[i_X] = Y
                    update[i_Y] = X
                    changed = True
    total += update[len(update) // 2]

print(total)
