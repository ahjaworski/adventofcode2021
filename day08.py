with open('input/input08.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
signal_patterns = []
output_values = []

for line in lines:
    output_value_line = line.split('| ')[1]
    output_values_from_line = output_value_line.split(' ')
    output_values = output_values + output_values_from_line

unique_output_values = []
unique_output_value_lengths = [2, 3, 4, 7]

for output_value in output_values:
    if len(output_value) in unique_output_value_lengths:
        unique_output_values.append(output_value)

print('Answer 1:', len(unique_output_values))


# part two


def word_contains_all_characters(word, characters, equals=False):
    count = 0
    for character in characters:
        if word.find(character) != -1:
            count += 1
    if equals:
        return count == len(characters) and count == len(word)
    else:
        return count == len(characters)


real_output_values = []

for line in lines:
    signals_line = line.split(' | ')[0]
    output_value_line = line.split('| ')[1]

    signals_from_line = signals_line.split(' ')
    output_values_from_line = output_value_line.split(' ')

    line_words = signals_from_line + output_values_from_line

    ones = [x for x in line_words if len(x) == 2]
    fours = [x for x in line_words if len(x) == 4]
    sevens = [x for x in line_words if len(x) == 3]
    eights = [x for x in line_words if len(x) == 7]

    line_words = [word for word in line_words if word not in (ones + fours + sevens + eights)]

    a = sevens[0]
    for letter in ones[0]:
        a = a.replace(letter, '')

    c = eights[0]
    six_letter_words = [x for x in line_words if len(x) == 6]
    six = [x for x in six_letter_words if word_contains_all_characters(x, ones[0]) is False][0]
    for letter in six:
        c = c.replace(letter, '')

    f = ones[0].replace(c, '')

    e = eights[0]
    nine = [x for x in six_letter_words if word_contains_all_characters(x, fours[0]) is True][0]
    for letter in nine:
        e = e.replace(letter, '')

    d = eights[0]
    zero = [x for x in six_letter_words if word_contains_all_characters(x, a + c + f + e) is True][0]
    for letter in zero:
        d = d.replace(letter, '')

    b = fours[0].replace(c, '').replace(d, '').replace(f, '')

    g = eights[0].replace(a, '').replace(b, '').replace(c, '').replace(d, '').replace(e, '').replace(f, '')


    def get_digit(word):
        if word_contains_all_characters(word, a + b + c + e + f + g, True):
            return '0'
        elif word_contains_all_characters(word, c + f, True):
            return '1'
        elif word_contains_all_characters(word, a + c + d + e + g, True):
            return '2'
        elif word_contains_all_characters(word, a + c + d + f + g, True):
            return '3'
        elif word_contains_all_characters(word, b + c + d + f, True):
            return '4'
        elif word_contains_all_characters(word, a + b + d + f + g, True):
            return '5'
        elif word_contains_all_characters(word, a + b + d + e + f + g, True):
            return '6'
        elif word_contains_all_characters(word, a + c + f, True):
            return '7'
        elif word_contains_all_characters(word, a + b + c + d + e + f + g, True):
            return '8'
        elif word_contains_all_characters(word, a + b + c + d + f + g, True):
            return '9'

    real_output_value = ''
    for value in output_values_from_line:
        real_output_value += get_digit(value)
    real_output_values.append(int(real_output_value))

print('Answer 2:', sum(real_output_values))
