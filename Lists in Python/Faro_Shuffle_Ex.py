name = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):

    first_half = []
    second_half = []

    for idx in range(1, len(name) - 1):
        card = name[idx]
        if idx < len(name) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_half[first_part_idx])
            first_part_idx += 1

    name = [name[0]] + shuffled + [name[-1]]
print(name)