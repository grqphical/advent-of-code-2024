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

# PART TWO


def is_safe_sequence(numbers):
    direction = 0
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) not in [1, 2, 3]:
            return False
        if abs(numbers[i] - numbers[i + 1]) == 0:
            return False
        if direction == 0:
            if numbers[i + 1] > numbers[i]:
                direction = 1
            elif numbers[i + 1] < numbers[i]:
                direction = -1
        else:
            if numbers[i + 1] > numbers[i] and direction == -1:
                return False
            elif numbers[i + 1] < numbers[i] and direction == 1:
                return False
    return True


safe_report_count = 0

for report in reports:
    numbers = [int(i) for i in report.split()]
    is_safe = is_safe_sequence(numbers)

    if not is_safe:
        # Try removing each number one at a time
        for i in range(len(numbers)):
            test_numbers = numbers[:i] + numbers[i + 1 :]
            if is_safe_sequence(test_numbers):
                is_safe = True
                break

    if is_safe:
        safe_report_count += 1

print(safe_report_count)
