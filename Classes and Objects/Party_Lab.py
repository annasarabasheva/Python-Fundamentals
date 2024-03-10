class People:
    def __init__(self):
        self.people = []


people = People()

while True:
    name = input()
    if name == "End":
        break

    people.people.append(name)


print(f"Going: {', '.join(people.people)}")
print(f"Total: {len(people.people)}")
