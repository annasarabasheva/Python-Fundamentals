cards = input().split(", ")
n = int(input())
if n > 0:
    for i in range(n):
        command_arg = input().split(", ")
        command = command_arg[0]
        if command == "Add":
            new_card = command_arg[1]
            if new_card not in cards:
                cards.append(new_card)
                print("Card successfully added")
            else:
                print("Card is already in the deck")
        elif command == "Remove":
            new_card = command_arg[1]
            if new_card in cards:
                cards.remove(new_card)
                print("Card successfully removed")
            else:
                print("Card not found")
        elif command == "Remove At":
            idx = int(command_arg[1])
            if idx in range(len(cards)):
                card = cards[idx]
                cards.remove(card)
                print("Card successfully removed")
            else:
                print("Index out of range")
        elif command == "Insert":
            idx = int(command_arg[1])
            new_card = command_arg[2]
            if idx in range(len(cards)):
                if new_card not in cards:
                    cards.insert(idx, new_card)
                    print("Card successfully added")
                else:
                    print("Card is already added")
            else:
                print("Index out of range")

    print(", ".join(cards))

else:
    print(", ".join(cards))