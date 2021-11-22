from tickets import *

def start():
    commands = {"view":view_tickets, "select":view_ticket}
    while True:
        print("Enter a Command:")
        command = input()
        if command in commands:
            commands[command]()


def view_tickets():
    tickets = get_tickets()
    if len(tickets) > 25:
        i = 0
        while i <= len(tickets):
            for t in tickets[i:i + 25]:
                print(t)
            command = input()
            if command == "next":
                i += 25
            elif command == "exit":
                break
    else:
        for t in tickets:
            print(t)

def view_ticket():
    id = input()
    print(get_ticket(id))

start()