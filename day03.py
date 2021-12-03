with open('input/input03.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
number_of_lines = len(lines)
gamma_rate = ''
epsilon_rate = ''
for i in range(0, len(lines[0])):
    sum_of_index = 0
    for line in lines:
        sum_of_index += int(line[i])
    if sum_of_index > (number_of_lines/2):
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

print('Answer 1:', int(gamma_rate, 2) * int(epsilon_rate, 2))


# part two
def get_lines_most_common(lines, index):
    number_of_lines = len(lines)

    sum_of_index = 0
    ones = []
    zeros = []
    for line in lines:
        number = int(line[index])
        sum_of_index += number
        if number == 1:
            ones.append(line)
        if number == 0:
            zeros.append(line)
    if len(lines) == 1:
        return lines
    if sum_of_index > (number_of_lines/2):
        return get_lines_most_common(ones, index+1)
    if sum_of_index < (number_of_lines/2):
        return get_lines_most_common(zeros, index+1)
    if sum_of_index == (number_of_lines/2) and len(lines) == 2:
        return ones
    if sum_of_index == (number_of_lines/2):
        return get_lines_most_common(ones, index+1)

def get_lines_least_common(lines, index):
    number_of_lines = len(lines)

    sum_of_index = 0
    ones = []
    zeros = []
    for line in lines:
        number = int(line[index])
        sum_of_index += number
        if number == 1:
            ones.append(line)
        if number == 0:
            zeros.append(line)
    if len(lines) == 1:
        return lines
    if sum_of_index > (number_of_lines/2):
        return get_lines_least_common(zeros, index+1)
    if sum_of_index < (number_of_lines/2):
        return get_lines_least_common(ones, index+1)
    if sum_of_index == (number_of_lines/2) and len(lines) == 2:
        return zeros
    if sum_of_index == (number_of_lines/2):
        return get_lines_least_common(zeros, index+1)

print('Answer 2:', int(get_lines_most_common(lines, 0)[0], 2) * int(get_lines_least_common(lines, 0)[0], 2))
