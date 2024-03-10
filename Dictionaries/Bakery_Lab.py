line = input().split()
dictionary = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    dictionary[key] = value


print(dictionary)

