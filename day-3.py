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
