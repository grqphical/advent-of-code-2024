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
