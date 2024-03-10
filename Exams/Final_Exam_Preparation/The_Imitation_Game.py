word = input()

while True:
    line = input()
    if line == "Decode":
        break

    command_arg = line.split("|")
    command = command_arg[0]
    if command == "Move":
        number_letter = int(command_arg[1])
        word = word[number_letter:] + word[0:number_letter]

    elif command == "Insert":
        index = int(command_arg[1])
        value = command_arg[2]
        word = word[:index] + value + word[index:]

    elif command == "ChangeAll":
        substring = command_arg[1]
        replacement = command_arg[2]
        word = word.replace(substring, replacement)


print(f"The decrypted message is: {word}")


