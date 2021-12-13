with open('input/input09.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
height_map = []


def find_adjacent_heights(x, y):
    adjacent_heights = []
    if x != 0:
        left = height_map[y][x-1]
        adjacent_heights.append(left)
    if x != len(height_map[0]) - 1:
        right = height_map[y][x+1]
        adjacent_heights.append(right)
    if y != 0:
        top = height_map[y-1][x]
        adjacent_heights.append(top)
    if y != len(height_map) - 1:
        bottom = height_map[y+1][x]
        adjacent_heights.append(bottom)
    return adjacent_heights

for line in lines:
    height_line = []
    for character in line:
        height_line.append(int(character))
    height_map.append(height_line)

low_points = []
low_points_yx = []

for y in range(len(height_map)):
    for x in range(len(height_map[y])):
        adjacent_heights = find_adjacent_heights(x, y)
        point = height_map[y][x]
        if all(point < i for i in adjacent_heights):
            low_points.append(point)
            low_points_yx.append([y, x])

print('Answer 1:', sum(low_points) + len(low_points))

# part two
bassin_yx = []
visited_yx = []
bassin_values = []
def get_surroundings(yx):
    if yx not in visited_yx:
        visited_yx.append(yx)
    else:
        return

    if height_map[yx[0]][yx[1]] < 9:
        bassin_yx.append(yx)
        if yx[1] > 0:
            get_surroundings([yx[0], yx[1] - 1])
        if yx[1] < len(height_map[0]) - 1:
            get_surroundings([yx[0], yx[1] + 1])
        if yx[0] > 0:
            get_surroundings([yx[0] - 1, yx[1]])
        if yx[0] < len(height_map) - 1:
            get_surroundings([yx[0] + 1, yx[1]])



def calculate_bassin(yx):
    get_surroundings(yx)
    for yx in bassin_yx:
        value = height_map[yx[0]][yx[1]]
        bassin_values.append(value)
    return len(bassin_values)


def multiplyList(list):
    result = 1
    for x in list:
        result = result * x
    return result


bassin_lengths = []
for low_point_yx in low_points_yx:
    bassin_len = calculate_bassin(low_point_yx)
    bassin_lengths.append(bassin_len)
    visited_yx = []
    bassin_yx = []
    bassin_values = []

bassin_lengths.sort(reverse=True)
print('Answer 2:', bassin_lengths[0] * bassin_lengths[1] * bassin_lengths[2])