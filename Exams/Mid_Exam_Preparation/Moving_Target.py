targets = [int(el) for el in input().split()]

while True:
    line = input()
    if line == "End":
        targets_strings = "|".join([str(el) for el in targets])
        print(targets_strings)
        break

    command_idx = line.split()
    command = command_idx[0]
    idx = int(command_idx[1])
    if command == "Shoot":
        if idx in range(len(targets)):
            power = int(command_idx[2])
            target = targets[idx]
            targets[idx] = target - power
            if targets[idx] <= 0:
                targets.remove(targets[idx])

    elif command == "Add":
        if idx in range(len(targets)):
            value = int(command_idx[2])
            targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        radius = int(command_idx[2])
        if idx in range(len(targets)) and (idx + radius) in range(len(targets)) and (idx-radius) in range(len(targets)):
            del targets[idx - radius:(idx + radius) + 1]
        else:
            print("Strike missed!")




