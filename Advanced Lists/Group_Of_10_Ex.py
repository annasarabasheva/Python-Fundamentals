from math import ceil
numbers = [int(el) for el in input().split(", ")]

low = 1
high = 10

groups_count = ceil(max(numbers) / 10)

for idx in range(1, groups_count + 1):
    grouped_numbers = [int(x) for x in numbers if low <= x <= high]
    print(f"Group of {10 * idx}'s: {grouped_numbers}")

    low += 10
    high += 10