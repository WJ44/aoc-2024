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
        else:
            for i, _ in enumerate(report):
                report_copy = report.copy()
                report_copy.pop(i)
                direction = 1 if report_copy[1] > report_copy[0] else -1
                report_copy_2 = report_copy.copy()
                report_copy_2.pop(0)
                safe = all(
                    1 <= (b - a) * direction <= 3
                    for a, b in zip(report_copy, report_copy_2)
                )
                if safe:
                    n_safe += 1
                    break

print(n_safe)
