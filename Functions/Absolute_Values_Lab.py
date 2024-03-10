numbers = input().split()
numbers_int = []


for i in numbers:
    n = float(i)
    a = abs(n)
    numbers_int.append(a)

print(numbers_int)