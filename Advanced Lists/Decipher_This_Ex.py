secret_message = input().split()

new_message = []

for e in secret_message:
    number = int(''.join(x for x in e if x.isdigit()))
    string = chr(number)
    result = e.replace(str(number), string)
    new_message.append(result)


def swap(str, i, j):
   list1 = list(str)
   list1[i], list1[j] = list1[j], list1[i]
   return ''.join(list1)

new_new = []
for el in new_message:
    second_letter = el[1]
    last_letter = el[-1]
    result = swap(el, 1, -1)
    new_new.append(result)

print(" ".join(new_new))

