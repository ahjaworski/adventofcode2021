with open('input/input01.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
increaseCount = 0
previousLine = None
for line in lines:
    if (previousLine is not None) and (int(line) > previousLine):
        increaseCount += 1
    previousLine = int(line)
print('Answer 1: ', increaseCount)

# part two
increaseSumCount = 0
previousSum = None
for idx, val in enumerate(lines):
    if idx >= 2:
        newSum = int(lines[idx]) + int(lines[idx - 1]) + int(lines[idx - 2])
        if previousSum is not None and newSum > previousSum:
            increaseSumCount += 1
        previousSum = newSum
print('Answer 2: ', increaseSumCount)
