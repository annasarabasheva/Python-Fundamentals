numbers = [int(el) for el in input().split()]

average = sum(numbers) / len(numbers)
best_nums = []

for i in range(len(numbers)):
    number = numbers[i]
    if number > average:
        best_nums.append(number)

if len(best_nums) <= 5:
    if len(best_nums) == 0:
        print("No")
        exit()
    best_nums.sort(reverse=True)
    best_nums = [str(el) for el in best_nums]
    print(" ".join(best_nums))

else:
    best_nums.sort(reverse=True)
    new_best_nums = []
    for e in range(len(best_nums)):
        element = best_nums[e]
        new_best_nums.append(element)
        if len(new_best_nums) > 4:
            break
    new_best_nums = [str(el) for el in new_best_nums]
    print(" ".join(new_best_nums))


