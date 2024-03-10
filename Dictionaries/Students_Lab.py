dic = {}
while True:
    line = input()
    if ":" not in line:
        line_two = line.split("_")
        line_two = " ".join(line_two)

        for key, value in dic.items():
            if key == line_two:
                for id, name in value.items():
                    print(f"{name} - {id}")
        break

    command_line = line.split(":")
    name = command_line[0]
    id = command_line[1]
    course = command_line[2]
    if course not in dic:
        dic[course] = {}
    dic[course][id] = name



