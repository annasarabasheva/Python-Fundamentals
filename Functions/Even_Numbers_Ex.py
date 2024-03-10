numbers = [int(el) for el in input().split()]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)