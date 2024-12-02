# PART ONE
reports = []

with open("day-2-input.txt", "r") as f:
    reports = f.readlines()

safe_report_count = 0

for report in reports:
    numbers = [int(i) for i in report.split(" ")]

    is_safe = True
    direction = 0

    for i, number in enumerate(numbers):
        if i == len(numbers) - 1:
            break

        next_num = numbers[i + 1]

        if direction == 0:
            if next_num > number:
                direction = 1
            elif next_num < number:
                direction = -1
        else:
            if next_num > number and direction == -1:
                is_safe = False
                break
            elif next_num < number and direction == 1:
                is_safe = False
                break
        if abs(number - next_num) == 0:
            is_safe = False
            break

        if abs(number - next_num) not in [1, 2, 3]:
            is_safe = False
            break

    if is_safe:
        safe_report_count += 1

print(safe_report_count)
