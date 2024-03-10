n = int(input())
positive = []
negative = []

counter_positive = 0
sum_negative = 0
for i in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
        counter_positive += 1
    else:
        negative.append(number)
        sum_negative += number



print(positive)
print(negative)
print(f"Count of positives: {counter_positive}")
print(f"Sum of negatives: {sum_negative}")