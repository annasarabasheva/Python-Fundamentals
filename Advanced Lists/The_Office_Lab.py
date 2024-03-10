numbers = [float(el) for el in input().split()]
num = float(input())

doubled_numbers = list(map(lambda x: x * num, numbers))
average = sum(doubled_numbers) / len(numbers)

positive_numbers = []

for el in doubled_numbers:
    if el >= average:
        positive_numbers.append(el)

if len(positive_numbers) >= len(numbers)/2:
    print(f"Score: {len(positive_numbers)}/{len(numbers)}. Employees are happy!")

else:
    print(f"Score: {len(positive_numbers)}/{len(numbers)}. Employees are not happy!")
