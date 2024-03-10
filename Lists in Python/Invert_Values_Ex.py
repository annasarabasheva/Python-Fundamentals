numbers = input().split()
list_int = []

for char in numbers:
    number = int(char) * -1
    list_int.append(number)


print(list_int)