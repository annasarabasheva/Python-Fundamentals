password = input()


def check_password(pas):

    special_characters = "!@#$%^&*()-+?_=,<>/"
    counter = 0

    flag = True
    if flag:
        if len(pas) < 6 or len(pas) > 10:
            print("Password must be between 6 and 10 characters")
            flag = False


        for el in pas:
            if el.isdigit():
                counter += 1
            if el in special_characters:
                print("Password must consist only of letters and digits")
                flag = False
                break



        if counter < 2:
            print("Password must have at least 2 digits")
            flag = False

    if flag:
        print("Password is valid")

check_password(password)