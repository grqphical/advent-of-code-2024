# PART ONE
left_list = []
right_list = []

with open("day-1-input.txt", "r") as f:
    for line in f.readlines():
        split = line.split("   ")
        left = split[0]
        right = split[1]

        left_list.append(int(left))
        right_list.append(int(right))

# sort the arrays
left_list.sort()
right_list.sort()

distances = []

for i in range(len(left_list)):
    right = right_list[i]
    left = left_list[i]

    if right > left:
        distances.append(right-left)
    else:
        distances.append(left-right)


sum = 0
for distance in distances:
    sum += distance

print(sum)

# PART TWO

sum = 0

for i in left_list:
    count = 0
    for j in right_list:
        if j == i:
            count += 1
    
    sum += i * count

print(sum)