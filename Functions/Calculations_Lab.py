operator = input()
first_number = int(input())
second_number = int(input())

def calculator(c, f_n, s_n):
    if c == "subtract":
        return (f_n - s_n)
    elif c == "divide":
        return (f_n // s_n)
    elif c == "multiply":
        return (f_n * s_n)
    elif c == "add":
        return (f_n + s_n)


print(calculator(operator,first_number,second_number))