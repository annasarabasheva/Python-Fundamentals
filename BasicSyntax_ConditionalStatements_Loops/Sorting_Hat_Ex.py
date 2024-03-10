while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    len_name = len(name)
    if len_name < 5:
        print(f"{name} goes to Gryffindor.")
    elif len_name == 5:
        print(f"{name} goes to Slytherin.")
    elif len_name == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len_name > 6:
        if name == "Voldemort":
            print("You must not speak of that name!")
            break
        else:
            print(f"{name} goes to Hufflepuff.")