n_safe = 0

with open("./02/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        report = [int(x) for x in line.rstrip().split()]
        direction = 1 if report[1] > report[0] else -1
        report_copy = report.copy()
        report_copy.pop(0)
        safe = all(1 <= (b - a) * direction <= 3 for a, b in zip(report, report_copy))
        if safe:
            n_safe += 1

print(n_safe)
