factor = int(input())
count = int(input())

list_numbers = []

for i in range(1, count+1):
    result = i * factor
    list_numbers.append(result)


print(list_numbers)