numbers = input().split()
number_int = []

for i in numbers:
    n = float(i)
    a = round(n)
    number_int.append(a)

print(number_int)