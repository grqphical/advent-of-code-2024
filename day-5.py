with open("day-5-input.txt", "r") as f:
    lines = f.readlines()
    groups = []
    current_group = []

    for line in lines:
        if line.strip() == "":
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line.strip())

    if current_group:
        groups.append(current_group)

rules_lines = groups[0]
update_lines = groups[1]

rules = []

# parse the rules
for line in rules_lines:
    split = line.split("|")
    first = int(split[0])
    second = int(split[1])

    rules.append((first, second))

# parse the updates
updates: list[list[int]] = []
for line in update_lines:
    split = line.split(",")
    update = [int(x) for x in split]
    updates.append(update)

correct_updates: list[list[int]] = []

for update in updates:
    is_correct = True
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue

        if update.index(rule[0]) > update.index(rule[1]):
            is_correct = False

    if is_correct:
        correct_updates.append(update)

sum = 0

for update in correct_updates:
    mid = (len(update) - 1) // 2
    sum += update[mid]

print(sum)
