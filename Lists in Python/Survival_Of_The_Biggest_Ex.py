numbers_all = input().split()
n = int(input())
list_numbers = []

for num in numbers_all:
    number = int(num)
    list_numbers.append(number)


for i in range(n):
    min_number = min(list_numbers)
    list_numbers.remove(min_number)


list_numbers_new = []
for el in list_numbers:
    new = str(el)
    list_numbers_new.append(new)

print(", ".join(list_numbers_new))