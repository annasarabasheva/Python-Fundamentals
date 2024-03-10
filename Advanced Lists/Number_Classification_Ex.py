numbers = [int(el) for el in input().split(", ")]
positives = []
negatives = []
even = []
odd = []

for el in numbers:
    if el >= 0:
        positives.append(str(el))
    if el % 2 == 0:
        even.append(str(el))
    if el % 2 != 0:
        odd.append(str(el))
    if el < 0:
        negatives.append(str(el))

p = ", ".join(positives)
n = ", ".join(negatives)
e = ", ".join(even)
o = ", ".join(odd)

print(f"Positive: {p}")
print(f"Negative: {n}")
print(f"Even: {e}")
print(f"Odd: {o}")

