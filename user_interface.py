import re
from tickets import *
from time import sleep
from collections import defaultdict

#Start the UI and read user commands
def start():
    commands = {"view":view_tickets, "select":view_ticket, "params":set_params}
    params = defaultdict(lambda: None)
    print("Zendesk Ticket Viewer - Zachary Adler")
    sleep(0.5)
    while True:
        sleep(0.5)
        print("\n\tTo view all tickets enter: view")
        print("\tTo view a specific ticket enter: select")
        print("\tTo search for tickets with specific parameters enter: params")
        print("\tTo quit the ticket viewer enter: quit\n")
        print("Enter a Command:")
        command = input()
        if command == "quit":
            print("")
            exit(0)
        elif command in commands:
            commands[command](params)
        else:
            print("\nInvalid Command")

#View all tickets with given parameters
def view_tickets(params):
    tickets = get_tickets(params)
    num = len(tickets)
    if num == 0:
        print("\nNo tickets found that match your criteria")
    elif num > 25:
        i = 0
        while i < num:
            print('\n')
            print(f"Showing Tickets {i + 1} through {i + 25} of {num}")
            for t in tickets[i:i+25]:
                print(t)
            print("\nTo view the next page enter: next")
            print("\nTo exit the ticket viewer enter: exit")
            command = input()
            if command == "next":
                i += 25
            elif command == "exit":
                break
    else:
        print('\n')
        for t in tickets:
            print(t)
    params.clear()

#View a specific ticket, requests a ticket id
def view_ticket(params):
    print("\nEnter a ticket id:")
    id = input()
    ticket = get_ticket(id)
    if not ticket:
        print("\nInvalid Ticket ID")
        return
    s = f"\n[{ticket.id}] {ticket.url}\n\nSubject: {ticket.subject}\nCreated: {ticket.created_at}\nStatus: {ticket.status}\nPriority: {ticket.priority}\nDescription: {ticket.description}"
    print(s)
    print("\nTo exit the ticket viewer enter: exit")
    while True:
        command = input()
        if command == "exit":
            return

#Gets user parameters and shows all matching tickets
def set_params(params):
    valid = {"open", "pending", "closed"}
    while True:
        print("\nI want tickets with STATUS (open, pending, closed):")
        print("Leave blank for all")
        status = input()
        if not status:
            break
        if status in valid:
            params["status"] = status
            break
        else:
            print("\nInvalid status")
    date = r"\d{2}/\d{2}/\d{4}"
    while True:
        print("\nI want tickets from after (MM/DD/YYYY):")
        print("Leave blank for all")
        after = input()
        if not after:
            break
        if re.match(date, after):
            params["after"] = after
            break
        print("\nInvalid format")
    while True:
        print("\nI want tickets from before (MM/DD/YYYY):")
        print("Leave blank for all")
        before = input()
        if not before:
            break
        if re.match(date, before):
            params["before"] = before
            break
        print("\nInvalid format")
    while True:
        print("\nSort tickets by (id, created_at, subject):")
        print("Leave blank to sort by id")
        valid = {"created_at", "id", "subject"}
        sort_by = input()
        if not sort_by:
            break
        if sort_by in valid:
            params["sort_by"] = sort_by
            break
    view_tickets(params)

start()