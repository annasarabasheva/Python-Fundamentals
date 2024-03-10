total_price = 0


while True:
    command = input()
    if command == "special" or command == "regular":
        if total_price == 0:
            print("Invalid order!")
            break
        if command == "special":
            with_taxes = total_price * 0.2
            total = (total_price + with_taxes) - ((total_price + with_taxes) * 0.1)
            print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {with_taxes:.2f}$\n-----------")
            print(f"Total price: {total:.2f}$")
            break

        with_taxes = total_price * 0.2
        total_total = total_price + with_taxes
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {with_taxes:.2f}$\n-----------")
        print(f"Total price: {total_total:.2f}$")
        break

    prices = float(command)
    if prices < 0:
        print("Invalid price!")
        continue
    total_price += prices


