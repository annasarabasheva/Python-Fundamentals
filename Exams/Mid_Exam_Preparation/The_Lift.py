def print_lift_states(list):
    current_state_lift = [str(el) for el in list]
    print(" ".join(current_state_lift))

people = int(input())
current_state_lift = [int(el) for el in input().split()]
total_free_seats = len(current_state_lift) * 4 - sum(current_state_lift)

for el in range(len(current_state_lift) + 1):

    if total_free_seats == 0 or people == 0:
        if people == 0 and total_free_seats > 0:
             print("The lift has empty spots!")
        elif people > 0 and total_free_seats == 0:
             print(f"There isn't enough space! {people} people in a queue!")
        print_lift_states(current_state_lift)
        break

    people_entered = 0
    people_in_current_wagon = current_state_lift[el]

    if people_in_current_wagon < 4 and people > 0:
        free_spaces = 4 - people_in_current_wagon
        if people > free_spaces:
            people -= free_spaces
            people_entered = free_spaces
        else:
            people_entered = people
            people = 0

        total_free_seats -= people_entered
        current_state_lift.pop(el)
        current_state_lift.insert(el, people_in_current_wagon + people_entered)


    elif people_in_current_wagon == 4 and people > 0:
        continue
