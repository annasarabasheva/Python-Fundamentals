n = int(input())
word = input()
lines_list = []
specific_list = []

for i in range(n):
    lines = input()
    lines_list.append(lines)
    if word in lines:
        specific_list.append(lines)




print(lines_list)
print(specific_list)