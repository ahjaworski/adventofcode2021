with open('input/input02.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
horizontal = 0
depth = 0

for line in lines:
    direction = line.split(' ', 1)[0]
    amount = int(line.split(' ', 1)[1])
    if direction == 'forward':
        horizontal += amount
    if direction == 'up':
        depth -= amount
    if direction == 'down':
        depth += amount

print('Answer 1: ', horizontal * depth)

# part two
horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction = line.split(' ', 1)[0]
    amount = int(line.split(' ', 1)[1])
    if direction == 'forward':
        horizontal += amount
        depth += aim * amount
    if direction == 'up':
        aim -= amount
    if direction == 'down':
        aim += amount

print('Answer 2: ', horizontal * depth)