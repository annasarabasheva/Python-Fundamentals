line = input().split()
dic = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    dic[key] = value


line_two = input().split()

for el in line_two:
    if el not in dic:
        print(f"Sorry, we don't have {el}")
    else:
        print(f"We have {dic[el]} of {el} left")

