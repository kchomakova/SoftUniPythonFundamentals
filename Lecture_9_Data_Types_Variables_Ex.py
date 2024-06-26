# Task 10: Gladiator Expenses
lost_fights = int(input())
PRICE_HELMET = float(input())
PRICE_SWORD = float(input())
PRICE_SHIELD = float(input())
PRICE_ARMOR = float(input())

total_expenses = 0
shield_repair_counter = 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        total_expenses += PRICE_HELMET

    if i % 3 == 0:
        total_expenses += PRICE_SWORD

    if i % 2 == 0 and i % 3 == 0:
        total_expenses += PRICE_SHIELD
        shield_repair_counter += 1
        if shield_repair_counter % 2 == 0:
            total_expenses += PRICE_ARMOR

print(f'Gladiator expenses: {total_expenses:.2f} aureus')
# Alternative way to see which are the days when both his helmet and sword are broken is as follows:
# if i % (2*3) == 0
# Also, we can have a counter for the number of times each element has been broken and use it to calculate
# the total cost.
# cnt_broken_helmet = lost_fights // 2
# cnt_broken_sword = lost_fights // 3
# cnt_broken_shield = lost_fights // 6
# cnt_broken_armor = cnt_broken_shield // 2

# Task 9: Snowballs
n_snowballs = int(input())

max_value = 0
winning_weight = 0
winning_time = 0
winning_quality = 0
for i in range(n_snowballs):
    w = int(input())
    t = int(input())
    q = int(input())

    value = (w / t) ** q

    if value > max_value:
        max_value = value
        winning_time = t
        winning_weight = w
        winning_quality = q

print(f"{winning_weight} : {winning_time} = {int(max_value)} ({winning_quality})")

# Task 8: Party Profit
group_size = int(input())
days = int(input())

total_profit = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5

    total_profit += 50 - group_size*2

    if i % 3 == 0:
        total_profit -= group_size*3

    if i % 5 == 0:
        if i % 3 == 0:
            total_profit += group_size*18
        else:
            total_profit += group_size*20

print(f"{group_size} companions received {int(total_profit/group_size)} coins each.")

# Task 6: Triples of Latin Letters
inp = int(input())

start_index = ord('a')
end_index = start_index + inp

for i in range(start_index, end_index):
    for j in range(start_index, end_index):
        for k in range(start_index, end_index):
            print(f'{chr(i)}{chr(j)}{chr(k)}')

#  Task 7: Water Overflow
CAPACITY_LITRES = 255
n = int(input())

remaining_capacity = CAPACITY_LITRES
for i in range(n):
    water_liters = int(input())
    if remaining_capacity < water_liters:
        print("Insufficient capacity!")
        continue

    remaining_capacity -= water_liters

print(CAPACITY_LITRES - remaining_capacity)

# More exercises Task 1: Exchange integers
first_number = int(input())
second_number = int(input())

print('Before:')
print(f'a = {first_number}')
print(f'b = {second_number}')
print('After:')
print(f'a = {second_number}')
print(f'b = {first_number}')

# More exercises Task 2: Prime Number Checker
inp_number = int(input())

is_prime = True
for i in range(2, inp_number):
    if inp_number % i == 0:
        is_prime = False

print(is_prime)

# More exercises Task 3: Decrypting Messages
key = int(input())
n = int(input())

message = ''
for i in range(n):
    letter = input()

    new_letter = chr(ord(letter) + key)
    message += new_letter

print(message)

# More exercises Task 4: Balanced Brackets
n = int(input())

brackets = ''
for _ in range(n):
    inp = input()
    if inp == '(' or inp == ')':
        brackets += inp

if brackets[0] == ')' or brackets[-1] == '(':
    print('UNBALANCED')
    exit()

for i in range(1,len(brackets)):
    if brackets[i] == brackets[i-1]:
        print('UNBALANCED')
        exit()
else:
    print('BALANCED')





