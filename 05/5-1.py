correct = []

with open("./05/input.txt", "r", encoding="utf-8") as file:
    rules, updates = file.read().split("\n\n")

    rules = [rule.split("|") for rule in rules.splitlines()]
    rules = [(int(X), int(Y)) for X, Y in rules]

    updates = [[int(x) for x in update.split(",")] for update in updates.splitlines()]

    for update in updates:
        for X, Y in rules:
            if X in update and Y in update and update.index(X) > update.index(Y):
                break
        else:
            correct.append(update)

total = 0
for update in correct:
    total += update[len(update) // 2]

print(total)
