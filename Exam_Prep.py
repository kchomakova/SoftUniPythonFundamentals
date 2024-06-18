# 1. Counter-Strike
initial_energy = int(input())

remaining_energy = initial_energy
won_battles = 0
while True:
    command = input()

    if command == 'End of battle':
        print(f'Won battles: {won_battles}. Energy left: {remaining_energy}')
        break

    elif remaining_energy >= int(command):
        won_battles += 1
        remaining_energy -= int(command)

        if won_battles % 3 == 0:
            remaining_energy += won_battles

    elif remaining_energy < int(command):
        print(f'Not enough energy! Game ends with {won_battles} won battles and {remaining_energy} energy')
        break


# 2. The Lift
def outcome(final_lift_state: list, remaining_people: int) -> str:
    if remaining_people == 0 and min(final_lift_state) < MAX_PEOPLE_IN_WAGON:
        return f"The lift has empty spots!\n{' '.join(list(map(str, final_lift_state)))}"

    if remaining_people == 0 and min(final_lift_state) == MAX_PEOPLE_IN_WAGON:
        return ' '.join(list(map(str, final_lift_state)))

    if remaining_people > 0 and min(final_lift_state) == MAX_PEOPLE_IN_WAGON:
        return f"""There isn't enough space! {remaining_people} people in a queue!\
        \n{' '.join(list(map(str, final_lift_state)))}"""


people = int(input())
initial_lift_state = list(map(int, input().split()))

MAX_PEOPLE_IN_WAGON = 4

current_lift_state = initial_lift_state
for i in range(len(initial_lift_state)):
    accommodated_people = min(MAX_PEOPLE_IN_WAGON - current_lift_state[i], people)
    people -= accommodated_people
    current_lift_state[i] += accommodated_people

result = outcome(current_lift_state, people)
print(result)


# 3. Numbers
some_numbers = list(map(int, input().split()))

avg = sum(some_numbers) / len(some_numbers)

greater_than_avg = list(filter(lambda x: x > avg, some_numbers))
output = sorted(greater_than_avg, reverse=True)

if len(output) > 5:
    output = output[:5]

if len(output) > 0:
    print(' '.join([str(i) for i in output]))
else:
    print('No')

