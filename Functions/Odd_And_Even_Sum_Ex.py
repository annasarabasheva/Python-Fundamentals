number = int(input())


def sum_even_odd(n):

    number_string = str(n)
    even_list = []
    odd_list = []

    for el in number_string:
        num = int(el)
        if num % 2 == 0:
            even_list.append(num)

        else:
            odd_list.append(num)

    sum_even = sum(even_list)
    sum_odd = sum(odd_list)
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


sum_even_odd(number)