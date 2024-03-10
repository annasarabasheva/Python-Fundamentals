numbers = [int(el) for el in input().split(", ")]
result = list(filter(lambda i: numbers[i] % 2 == 0, range(len(numbers))))

print(result)