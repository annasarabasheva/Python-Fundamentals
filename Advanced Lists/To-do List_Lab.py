to_do_list = []
numbers = []

while True:
    command_args = input().split("-")
    command = command_args[0]
    if command == "End":
        to_do_list.sort()
        break

    args = command_args[1]
    to_do_list.append(command_args)
    command_new = int(command_args[0])
    if command_new > 10 or command_new < 1:
        continue


new_list = []


for el in range(len(to_do_list)):
    element = to_do_list[el]
    for ne in element:
        del element[0]
        new_list.append(element[0])



print(new_list)
