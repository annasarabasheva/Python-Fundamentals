import sys
max_size = sys.maxsize
min_size = -sys.maxsize - 1

numbers = [int(el) for el in input().split()]

while True:
    line = input()
    if line == "end":
        numbers_strings = [str(e) for e in numbers]
        print(", ".join(numbers_strings))
        break
    elif line == "decrease":
       # numbers = list(map(lambda x:min_size if  x - 1 <min_size else x-1, numbers))
       numbers = list(map(lambda x: x-1, numbers))
       continue

    command_arg = line.split()
    command = command_arg[0]
    index_one = int(command_arg[1])
    index_two = int(command_arg[2])

    if command == "swap":
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

    elif command == "multiply":
        element_one = numbers[index_one]
        element_two = numbers[index_two]
        multiply = element_one * element_two
        numbers[index_one] = multiply



