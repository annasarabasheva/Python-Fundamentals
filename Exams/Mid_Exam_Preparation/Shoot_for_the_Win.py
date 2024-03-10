targets = [int(el) for el in input().split()]

counter = 0
while True:
    command = input()
    if command == "End":
        for i in range(len(targets)):
            target = targets[i]
            if target == -1:
                counter += 1
        targets_strings = " ".join([str(el) for el in targets])
        print(f"Shot targets: {counter} -> {targets_strings}")
        break
    index = int(command)
    if index in range(len(targets)):
        current_target = targets[index]
        targets[index] = -1
        for i in range(len(targets)):
            element = targets[i]
            old_element = element
            if element != -1:
                if element > current_target:
                    element -= current_target
                    targets[i] = element

                elif element <= current_target:
                    element += current_target
                    targets[i] = element
