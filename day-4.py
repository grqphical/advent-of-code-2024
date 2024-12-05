with open("day-4-input.txt", "r") as f:
    data = f.read()

count = 0

# find all horizontal instances
count += data.count("XMAS") + data.count("SAMX")

# convert it to an array
word_search = [list(line) for line in data.split("\n")]

# find all vertical instances
row_length = len(word_search[0])
for i in range(row_length):
    column_str = ""
    for j in range(len(word_search)):
        column_str += word_search[j][i]

    count += column_str.count("XMAS") + column_str.count("SAMX")

    # find all diagonal instances
    n = len(word_search)
    m = len(word_search[0])

word = "XMAS"
# Check diagonals from top-left to bottom-right
for i in range(n):
    for j in range(m):
        if i + len(word) <= n and j + len(word) <= m:
            if all(word_search[i + k][j + k] == word[k] for k in range(len(word))):
                count += 1

# Check diagonals from top-right to bottom-left
for i in range(n):
    for j in range(m):
        if i + len(word) <= n and j - len(word) >= -1:
            if all(word_search[i + k][j - k] == word[k] for k in range(len(word))):
                count += 1

word = "SAMX"
# Check diagonals from top-left to bottom-right
for i in range(n):
    for j in range(m):
        if i + len(word) <= n and j + len(word) <= m:
            if all(word_search[i + k][j + k] == word[k] for k in range(len(word))):
                count += 1

# Check diagonals from top-right to bottom-left
for i in range(n):
    for j in range(m):
        if i + len(word) <= n and j - len(word) >= -1:
            if all(word_search[i + k][j - k] == word[k] for k in range(len(word))):
                count += 1

print(count)

# PART TWO
count = 0

for row in range(len(word_search)):
    for col in range(len(word_search[row])):
        if row + 2 < len(word_search) and col + 2 < len(word_search[row]):
            if word_search[row][col] == "M" and word_search[row][col + 2] == "S":
                if word_search[row + 1][col + 1] == "A":
                    if (
                        word_search[row + 2][col] == "M"
                        and word_search[row + 2][col + 2] == "S"
                    ):
                        count += 1
            elif word_search[row][col] == "S" and word_search[row][col + 2] == "S":
                if word_search[row + 1][col + 1] == "A":
                    if (
                        word_search[row + 2][col] == "M"
                        and word_search[row + 2][col + 2] == "M"
                    ):
                        count += 1
            elif word_search[row][col] == "M" and word_search[row][col + 2] == "M":
                if word_search[row + 1][col + 1] == "A":
                    if (
                        word_search[row + 2][col] == "S"
                        and word_search[row + 2][col + 2] == "S"
                    ):
                        count += 1
            elif word_search[row][col] == "S" and word_search[row][col + 2] == "M":
                if word_search[row + 1][col + 1] == "A":
                    if (
                        word_search[row + 2][col] == "S"
                        and word_search[row + 2][col + 2] == "M"
                    ):
                        count += 1


print(count)
