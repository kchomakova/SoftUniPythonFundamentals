import random

computer_random = random.randint(1, 100)

while True:
    player_input = input('Guess the number (1-100): ')
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue

    player_input = int(player_input)
    if player_input == computer_random:
        print('You guess it!')
        break
    elif player_input > computer_random:
        print('Too high!')
    else:
        print('Too low!')
