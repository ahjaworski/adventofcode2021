with open('input/input07.txt') as f:
    lines = [i.strip() for i in f.readlines()]


# part one
crabs = [int(x) for x in lines[0].split(",")]

min_position = min(crabs)
max_position = max(crabs)

best_position = 0
best_sum_of_fuel = 0
for i in range(min_position, max_position + 1):
    sum_of_fuel = 0
    for crab in crabs:
        sum_of_fuel += abs(i - crab)

    if best_position == 0 or sum_of_fuel < best_sum_of_fuel:
        best_position = i
        best_sum_of_fuel = sum_of_fuel

print('Answer 1:', best_sum_of_fuel)


# part two
best_position = 0
best_sum_of_fuel = 0
for i in range(min_position, max_position + 1):
    sum_of_fuel = 0
    for crab in crabs:
        distance = abs(i - crab)
        sum_of_fuel += ((0.5 * distance) * (distance + 1))

    if best_position == 0 or sum_of_fuel < best_sum_of_fuel:
        best_position = i
        best_sum_of_fuel = sum_of_fuel

print('Answer 2:', best_sum_of_fuel)