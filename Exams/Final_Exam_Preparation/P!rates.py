towns = {}
while True:
    line = input()
    if line == "Sail":
        break

    command_arg = line.split("||")
    city = command_arg[0]
    population = int(command_arg[1])
    gold = int(command_arg[2])
    if city not in towns:
        towns[city] = [population, gold]
    else:
        towns[city][0] += population
        towns[city][1] += gold

while True:
    new_line = input()
    if new_line == "End":
        break

    command_arg = new_line.split("=>")
    command = command_arg[0]
    if command == "Plunder":
        town = command_arg[1]
        people = int(command_arg[2])
        gold = int(command_arg[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        towns[town][0] -= people
        towns[town][1] -= gold
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            del towns[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        town = command_arg[1]
        gold = int(command_arg[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        towns[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.")


if len(towns) > 0:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for t in towns:
        print(f"{t} -> Population: {towns[t][0]} citizens, Gold: {towns[t][1]} kg")

elif len(towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

