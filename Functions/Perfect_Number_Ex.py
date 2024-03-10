number = int(input())

def perfect_number(n):

    dividors = []


    for i in range(1, n):
        if n % i == 0:
            dividors.append(i)


    if sum(dividors) == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_number(number)