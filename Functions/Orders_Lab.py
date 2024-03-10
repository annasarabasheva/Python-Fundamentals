product = input()
quantity = int(input())

def total_price(p, q):
    if p == "coffee":
        return q * 1.50
    elif p == "water":
        return q * 1.00
    elif p == "coke":
        return q * 1.40
    elif p == "snacks":
        return q * 2.00

print(f"{(total_price(product, quantity)):.2f}")
