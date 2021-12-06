with open('input/input06.txt') as f:
    lines = [i.strip() for i in f.readlines()]

# part one
fish = [int(x) for x in lines[0].split(",")]


def add_day():
    for i in range(0, len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1


def add_days(number_of_days):
    for i in range(0, number_of_days):
        add_day()


add_days(80)
print('Answer 1:', len(fish))

# day 2
fish = [int(x) for x in lines[0].split(",")]


def get_fish_count(fish_input):
    fish_count = {}
    for i in range(0, 9):
        fish_count[i] = fish_input.count(i)
    return fish_count


fish_count = get_fish_count(fish)


def add_a_day():
    babies = fish_count[0]
    for i in range(0, 8):
        fish_count[i] = fish_count[i + 1]
    fish_count[6] += babies
    fish_count[8] = babies


def add_number_of_days(number_of_days):
    for i in range(0, number_of_days):
        add_a_day()


add_number_of_days(256)
print('Answer 2:', sum(fish_count.values()))
