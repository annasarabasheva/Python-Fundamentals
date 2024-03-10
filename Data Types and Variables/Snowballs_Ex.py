import sys

number_snowballs = int(input())
max_number = -sys.maxsize

for i in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight // time) ** quality
    if result > max_number:
        max_number = result
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_number} ({max_quality})")