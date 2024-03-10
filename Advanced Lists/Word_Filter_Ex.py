words = input().split()
even_len = [el for el in words if len(el) % 2 == 0]

print("\n".join(even_len))