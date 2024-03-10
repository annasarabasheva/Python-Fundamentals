elements = input().split()

counter_moves = 0
continue_game = True
while True:
    line = input()
    if line == "end":
        break
    if len(elements) == 0:
        continue
    command_arg = line.split()
    first_index = int(command_arg[0])
    second_index = int(command_arg[1])
    if first_index in range(len(elements)) and second_index in range(len(elements)) and first_index != second_index:
        first_element = elements[first_index]
        second_element = elements[second_index]
        counter_moves += 1
        if len(elements) > 0:
            if first_element == second_element:
                elements.remove(first_element)
                elements.remove(second_element)
                print(f"Congrats! You have found matching elements - {first_element}!")
            else:
                print("Try again!")
        if len(elements) == 0:
            print(f"You have won in {counter_moves} turns!")
            continue_game = False

    elif first_index == second_index or first_index not in range(len(elements)) or second_index not in range(len(elements)):
        counter_moves += 1
        middle = len(elements) // 2
        elements.insert(middle, f"-{counter_moves}a")
        elements.insert(middle, f"-{counter_moves}a")
        print("Invalid input! Adding additional elements to the board")


if continue_game:
    print('Sorry you lose :(')
    print(" ".join(elements))
