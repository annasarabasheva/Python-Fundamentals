dic = {}
while True:
    line = input()
    if "-" not in line:
        n = int(line)
        for i in range(n):
            person = input()
            if person not in dic:
                print(f"Contact {person} does not exist.")
            else:
                print(f"{person} -> {dic[person]}")
        break
    command_line = line.split("-")
    name = command_line[0]
    number = command_line[1]
    dic[name] = number

