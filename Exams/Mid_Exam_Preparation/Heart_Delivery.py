neighbourhood = [int(el) for el in input().split("@")]
counter = 0
last_index = 0
while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {last_index}.")
        if sum(neighbourhood) == 0:
            print("Mission was successful.")
        else:
            for e in range(len(neighbourhood)):
                element = neighbourhood[e]
                if element > 0:
                    counter += 1
            print(f"Cupid has failed {counter} places.")
        break
    jump_arg = command.split()
    index = int(jump_arg[1]) + last_index
    if index not in range(len(neighbourhood)):
        index = 0
    if neighbourhood[index] == 0:

        print(f"Place {index} already had Valentine's day.")
        last_index = index
        continue
    neighbourhood[index] -= 2
    if neighbourhood[index] == 0:
        print(f"Place {index} has Valentine's day.")
    last_index = index
