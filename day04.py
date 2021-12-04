with open('input/input04.txt') as f:
    lines = f.readlines()

# part one
def get_bingo_card(lines):
    rows = []
    for i in range(0, 5):
        row = [int(lines[i][0:2]), int(lines[i][3:5]), int(lines[i][6:8]), int(lines[i][9:11]), int(lines[i][12:14])]
        rows.append(row)

    columns = []
    for i in range(0, 5):
        column = [int(lines[0][i*3:i*3 + 2]), int(lines[1][i*3:i*3 + 2]), int(lines[2][i*3:i*3 + 2]),
                  int(lines[3][i*3:i*3 + 2]), int(lines[4][i*3:i*3 + 2])]
        columns.append(column)

    return rows + columns

bingo_cards = []
j = 1
while j < len(lines):
    line = lines[j]
    if len(line) == 0 or line == '\n':
        j += 1
        continue
    else:
        endLine = j + 5
        bingo_card = get_bingo_card(lines[j:endLine])
        bingo_cards.append(bingo_card)
        j = endLine

bingo_input = lines[0].split(',')
called_numbers = []
last_called_number = None
winner_card = None

for input in bingo_input:
    last_called_number = int(input)
    called_numbers.append(last_called_number)
    for card in bingo_cards:
        for row in card:
            result = all(elem in called_numbers for elem in row)
            if result:
                winner_card = card
                break

    if winner_card is not None:
        break

if winner_card is not None:
    winner_card_rows = []
    for row in winner_card:
        winner_card_rows.extend(row)
    winner_card_rows = set(winner_card_rows)
    for called_number in called_numbers:
        winner_card_rows.discard(called_number)

    print('Answer 1:', sum(winner_card_rows) * last_called_number)


# part two
called_numbers = []
last_called_number = None
winner_cards = []

for input in bingo_input:
    last_called_number = int(input)
    called_numbers.append(last_called_number)
    for card in bingo_cards:
        for row in card:
            result = all(elem in called_numbers for elem in row)
            if result:
                winner_cards.append(card)
                bingo_cards.remove(card)
                break

        if len(bingo_cards) == 0:
            break

    if len(bingo_cards) == 0:
        break

last_winner_card = winner_cards[-1]

if last_winner_card is not None:
    winner_card_rows = []
    for row in last_winner_card:
        winner_card_rows.extend(row)
    winner_card_rows = set(winner_card_rows)

    for called_number in called_numbers:
        winner_card_rows.discard(called_number)

    print('Answer 2:', sum(winner_card_rows) * last_called_number)