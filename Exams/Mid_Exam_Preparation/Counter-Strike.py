initial_energy = int(input())

counter_won_battles = 0
while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {counter_won_battles}. Energy left: {initial_energy}" )
        break
    distance = int(command)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {counter_won_battles} won battles and {initial_energy} energy")
        break
    initial_energy -= distance
    counter_won_battles += 1
    if counter_won_battles % 3 == 0:
        initial_energy += counter_won_battles



