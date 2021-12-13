with open('input/input10.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
open_chars = []
corrupted_chars_in_lines = []


def get_opening_char(closing_char):
    if closing_char == ')':
        return '('
    elif closing_char == ']':
        return '['
    elif closing_char == '>':
        return '<'
    elif closing_char == '}':
        return '{'
    else:
        return None


def is_opening_char(opening_char):
    return opening_char in ['(', '[', '<', '{']


def is_closing_char(closing_char):
    valid_closing_char = [')', ']', '>', '}'].index(closing_char) != -1
    expected_closing_char = open_chars[-1] == get_opening_char(closing_char)
    return valid_closing_char and expected_closing_char


for i in range(len(lines)):
    open_chars = []
    line = lines[i]
    for char in line:
        if is_opening_char(char):
            open_chars.append(char)
        elif is_closing_char(char):
            open_chars.pop()
        else:
            corrupted_chars_in_lines.append([i, char])

scores = []
for i in range(len(lines)):
    for corrupted_char in corrupted_chars_in_lines:
        if corrupted_char[0] == i:
            corrupted_character = corrupted_char[1]
            if corrupted_character == ')':
                scores.append(3)
            elif corrupted_character == ']':
                scores.append(57)
            elif corrupted_character == '>':
                scores.append(25137)
            elif corrupted_character == '}':
                scores.append(1197)
            break

print('Answer 1:', sum(scores))


# part two

finished_lines = []
for i in range(len(lines)):
    for corrupted_chars_in_line in corrupted_chars_in_lines:
        if corrupted_chars_in_line[0] == i:
            finished_lines.append(i)


def get_closing_char(opening_char):
    if opening_char == '(':
        return ')'
    elif opening_char == '[':
        return ']'
    elif opening_char == '<':
        return '>'
    elif opening_char == '{':
        return '}'
    else:
        return None


scores_for_lines = []
for i in range(len(lines)):
    if i not in set(finished_lines):
        score_for_line = 0
        open_chars = []
        needed_closing_chars = []
        line = lines[i]
        for char in line:
            if is_opening_char(char):
                open_chars.append(char)
            elif is_closing_char(char):
                open_chars.pop()

        for open_char in reversed(open_chars):
            needed_closing_chars.append(get_closing_char(open_char))

        for needed_closing_char in needed_closing_chars:
            score_for_line *= 5
            if needed_closing_char == ')':
                score_for_line += 1
            elif needed_closing_char == ']':
                score_for_line += 2
            elif needed_closing_char == '>':
                score_for_line += 4
            elif needed_closing_char == '}':
                score_for_line += 3
        scores_for_lines.append(score_for_line)

scores_for_lines.sort()

print('Answer 2:', scores_for_lines[int((len(scores_for_lines) - 1) / 2)])
