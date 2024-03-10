class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_emails = []

while True:
    line = input()
    if line == "Stop":
        break
    information = line.split()
    sender = information[0]
    receiver = information[1]
    content = information[2]
    email = Email(sender, receiver, content)
    list_emails.append(email)


indices = [int(el) for el in input().split(", ")]

for index, email in enumerate(list_emails):
    for el in indices:
        if index == el:
            email.send()
    print(email.get_info())
