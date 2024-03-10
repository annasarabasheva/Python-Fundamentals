numbers = input().split(", ")

for el in numbers:

    if el == str(el)[::-1]:
        print("True")
    else:
        print("False")
