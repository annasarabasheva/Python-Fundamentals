divisor = int(input())
bound = int(input())
number = []
for i in range(divisor, bound + 1):
    if i % divisor == 0 and bound >= i > 0:
        number += [i]
print(max(number))

