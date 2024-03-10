numbers_str = input().split(", ")
beggars_number = int(input())

beggars = [0] * beggars_number

for i in range(len(numbers_str)):
    beggar_i = i % beggars_number
    num = int(numbers_str[i])
    beggars[beggar_i] += num


print(beggars)