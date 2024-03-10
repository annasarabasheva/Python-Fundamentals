
dic = {}
while True:
    line = input()
    if line == "end":
        break
    command_line = line.split(" : ")
    course = command_line[0]
    name = command_line[1]
    if course not in dic:
        dic[course] = [name]
    else:
        dic[course].append(name)


for key, value in dic.items():
    print(f"{key}: {len(value)}")
    for val in value:
        print(f"-- {val}")
