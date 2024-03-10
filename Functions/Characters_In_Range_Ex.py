first = input()
second = input()

def ascii_table(a,b):

    list_char = []

    for i in range(ord(a) + 1, ord(b)):
        text = chr(i)
        list_char.append(text)


    print(" ".join(list_char))

ascii_table(first, second)