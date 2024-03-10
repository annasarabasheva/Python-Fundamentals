text = input()
digit = ""
letters = ""
symbols = ""
for el in text:
    if el.isdigit():
        digit += el

    elif el.isalpha():
        letters += el
    else:
        symbols += el

print(digit)
print(letters)
print(symbols)