# 1. Invert Values
input_str = input()

lst = input_str.split()
output_lst = []

for s in lst:
    output_lst.append(int(s)*-1)

print(output_lst)


# 2. Multiples List
factor = int(input())
cnt = int(input())

lst = []
multiplier = 1
for _ in range(cnt):
    lst.append(multiplier*factor)
    multiplier += 1

lst.sort()
print(lst)


# 3. Football Cards
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
#Alternative syntax:
# team_a = ['A-' + str(num) for num in range(1,12)]
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards = input()
cards_lst = cards.split()

game_terminated = False
for card in cards_lst:
    if card in team_a:
        team_a.remove(card)
    if card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_terminated:
    print('Game was terminated')


# 4. Number Beggars
numbers = input()
cnt_beggars = int(input())

numbers_lst_str = numbers.split(', ')
numbers_lst_int = [int(i) for i in numbers_lst_str]
len_lst = len(numbers_lst_str)

idxs = []
for _ in range(cnt_beggars):
    idxs.append([])

output_lst = []
for i in range(cnt_beggars):
    for j in range(i, len_lst, cnt_beggars):
        idxs[i].append(numbers_lst_int[j])
    output_lst.append(sum(idxs[i]))

print(output_lst)


# 5. Faro Shuffle
deck = input()
shuffles = int(input())

deck_lst = deck.split()

input_lst = deck_lst
output_lst = []
for i in range(shuffles):
    first_half = input_lst[:int(len(input_lst) / 2)]
    second_half = input_lst[int(len(input_lst) / 2):]

    for j in range(len(first_half)):
        output_lst.extend([first_half[j], second_half[j]])
    input_lst = output_lst
    output_lst = []

print(input_lst)


# 6. Survival of the Biggest
ints = input()
n = int(input())

ints_lst = ints.split()
ints_lst_int = [int(i) for i in ints_lst]

ints_lst_int_copy = ints_lst_int.copy()
ints_lst_int_copy.sort(reverse=True)

for _ in range(n):
    ints_lst_int_copy.pop()

output_lst = []
for i in ints_lst_int:
    if i in ints_lst_int_copy:
        output_lst.append(i)

for i in range(len(output_lst)):
    if i < len(output_lst) -1:
        print(output_lst[i], end=', ')
    else:
        print(output_lst[i])


# 7. Easter Gifts
gifts = input()

gifts_lst = gifts.split()

command = ''
gift = ''
while command != 'No Money':
    command = input()
    split_command = command.split()
    gift = split_command[1]

    if split_command[0] == 'OutOfStock':
        if gift in gifts_lst:
            target_indexes = [i for i,n in enumerate(gifts_lst) if n == gift]
            for i in target_indexes:
                gifts_lst[i] = 'None'
    elif split_command[0] == 'Required':
        if 0 <= int(split_command[2]) <= len(gifts_lst) -1:
            gifts_lst[int(split_command[2])] = gift
    elif split_command[0] == 'JustInCase':
        gifts_lst.pop()
        gifts_lst.append(gift)

for i in gifts_lst:
    if i != 'None':
        print(i, end = ' ')


# 8. Seize the Fire
fire = input()
water = int(input())

fire_lst = fire.split('#')

fire_lst_final = []
for i in fire_lst:
    i_split = i.split(' = ')
    valid = ((i_split[0] == 'High' and 81 <= int(i_split[1]) <= 125) or
             (i_split[0] == 'Medium' and 51 <= int(i_split[1]) <= 80) or
             (i_split[0] == 'Low' and 1 <= int(i_split[1]) <= 50))
    if valid:
        fire_lst_final.append(i_split)

remaining_water = water
total_effort = 0
cells = []
for c in fire_lst_final:
    cell_value = int(c[1])
    if remaining_water >= cell_value:
        remaining_water -= cell_value
        total_effort += 0.25*cell_value
        cells.append(cell_value)

print('Cells:')
for cell in cells:
    print(f'- {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {sum(cells)}')


# 10. Bread Factory
events = input()

INITIAL_ENERGY = 100
INITIAL_COINS = 100
events_lst = events.split('|')

current_energy = INITIAL_ENERGY
current_coins = INITIAL_COINS
success = True
for i in events_lst:
    components = i.split('-')
    event = components[0]
    quantity = int(components[1])
# Alternative syntax: event, quantity = i.split('-')

    if event == 'rest':
        gained_energy = min(quantity, INITIAL_ENERGY - current_energy)
        current_energy += gained_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
    elif event == 'order':
        if current_energy >= 30:
            current_coins += quantity
            current_energy -= 30
            print(f'You earned {quantity} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if current_coins >= quantity:
            print(f'You bought {event}.')
            current_coins -= quantity
        else:
            print(f'Closed! Cannot afford {event}.')
            success = False
            break

if success:
    print('Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {current_energy}')


# More exercises: 1. Zeros to Back
numbers = input()
numbers_lst = numbers.split(', ')

zeros = []
non_zeros = []
for i in range(len(numbers_lst)):
    if numbers_lst[i] == '0':
        zeros.append('0')
    else:
        non_zeros.append(numbers_lst[i])

final_list = non_zeros + zeros
print([int(i) for i in final_list])


# More exercises: 1. Messaging
numbers = input()
chars = input()

numbers_lst = numbers.split()
new_list = []
for i in range(len(numbers_lst)):
    new_list.append([])
    for j in range(len(numbers_lst[i])):
        new_list[i].append(int(numbers_lst[i][j]))

sums = []
for i in new_list:
    sums.append(sum(i))

chars_lst = []
for i in range(len(chars)):
    chars_lst.append(chars[i])

message_lst = []
for i in sums:
    idx = i % len(chars_lst)
    message_lst.append(chars_lst[idx])
    chars_lst.pop(idx)

message = "".join(message_lst)
print(message)


# More exercises: 3. Car Race

