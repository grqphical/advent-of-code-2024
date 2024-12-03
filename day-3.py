import re

# PART ONE
with open("day-3-input.txt", "r") as f:
    data = f.read()

p = re.compile(r"mul\((\d*),(\d*)\)")
matches = p.findall(data)

sum = 0

for match in matches:
    sum += int(match[0]) * int(match[1])

print(sum)

# PART TWO
with open("day-3-input.txt", "r") as f:
    data = f.read()

mul = re.compile(r"mul\((\d*),(\d*)\)")
matches = mul.findall(data)
mul_positions = [(match.start(), "mul") for match in mul.finditer(data)]
do_positions = [(match.start(), "do") for match in re.finditer(r"do\(\)", data)]
dont_positions = [(match.start(), "dont") for match in re.finditer(r"don't\(\)", data)]

instructions = sorted(mul_positions + do_positions + dont_positions, key=lambda x: x[0])
instructions = [instr[1] for instr in instructions]

mul_counter = 0
sum = 0
enabled = True
for instruction in instructions:
    if instruction == "mul":
        if enabled:
            sum += int(matches[mul_counter][0]) * int(matches[mul_counter][1])
        mul_counter += 1

    elif instruction == "dont":
        enabled = False
    elif instruction == "do":
        enabled = True

print(sum)
