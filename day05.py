with open('input/input05.txt') as f:
    lines = [i.strip() for i in f.readlines()]


# part one
def get_range(first, second):
    if (first < second):
        return list(range(first, second))
    else:
        return list(range(second, first))


def get_start_end_points(lines):
    points = []
    for line in lines:
        start = line.split(' -> ')[0]
        end = line.split(' -> ')[1]
        start_x = int(start.split(',')[0])
        start_y = int(start.split(',')[1])
        end_x = int(end.split(',')[0])
        end_y = int(end.split(',')[1])

        points.append([[start_x, start_y], [end_x, end_y]])
    return points


def create_point_lines(start_end_points, include_diagonal):
    point_lines = []
    for start_end_point in start_end_points:
        point_line = []
        start_x = start_end_point[0][0]
        start_y = start_end_point[0][1]
        end_x = start_end_point[1][0]
        end_y = start_end_point[1][1]
        if start_x == end_x:
            y_range = get_range(start_y, end_y)
            y_range.append((y_range[-1]) + 1)
            for y in y_range:
                point_line.append([start_x, y])
        elif start_y == end_y:
            x_range = get_range(start_x, end_x)
            x_range.append((x_range[-1]) + 1)
            for x in x_range:
                point_line.append([x, start_y])
        elif include_diagonal is True and start_x != end_x and start_y != end_y:
            if start_x > end_x:
                temp_start_x =  start_x
                temp_start_y =  start_y
                start_x = end_x
                start_y = end_y
                end_x = temp_start_x
                end_y = temp_start_y

            x_range = get_range(start_x, end_x)
            x_range.append((x_range[-1]) + 1)
            y_range = get_range(start_y, end_y)
            y_range.append((y_range[-1]) + 1)

            if start_y < end_y:
                for i in range(0, len(x_range)):
                    point_line.append([x_range[i], y_range[i]])
            else:
                for i in range(0, len(x_range)):
                    point_line.append([x_range[i], y_range[(len(y_range)-1)-i]])

        if len(point_line) != 0:
            point_lines.append(point_line)

    return point_lines


start_end_points = get_start_end_points(lines)
point_lines = create_point_lines(start_end_points, False)

seen_points = set()
overlapping_points = set()
for point_line in point_lines:
    for point in point_line:
        string_point = str(point[0]) + ',' + str(point[1])
        if string_point in seen_points:
            overlapping_points.add(string_point)
        else:
            seen_points.add(string_point)

print('Answer 1:', len(overlapping_points))


# part two
point_lines = create_point_lines(start_end_points, True)

seen_points = set()
overlapping_points = set()

for point_line in point_lines:
    for point in point_line:
        string_point = str(point[0]) + ',' + str(point[1])
        if string_point in seen_points:
            overlapping_points.add(string_point)
        else:
            seen_points.add(string_point)

print('Answer 2:', len(overlapping_points))
