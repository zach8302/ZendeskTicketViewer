import re
from tickets import *
from collections import defaultdict

def start():
    commands = {"view":view_tickets, "select":view_ticket, "params":set_params}
    params = defaultdict(lambda: None)
    print("Zendesk Ticket Viewer\nTo view all tickets enter: view\nTo view a specific ticket enter: select\nTo set search parameters enter: params")
    while True:
        print("Enter a Command:")
        command = input()
        if command in commands:
            commands[command](params)

def view_tickets(params):
    tickets = get_tickets(params)
    num = len(tickets)
    if num == 0:
        print("No tickets found that match your criteria\n")
    elif num > 25:
        i = 0
        while i < num:
            print('\n')
            print(f"Showing Tickets {i + 1} through {i + 25} of {num}")
            for t in tickets[i:i+25]:
                print(t)
            print("Enter next to view the next page")
            print("Enter exit to exit the ticket viewer")
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

def view_ticket(params):
    id = input()
    ticket = get_ticket(id)
    s = f"\n[{ticket.id}] {ticket.url}\n\nSubject: {ticket.subject}\nCreated: {ticket.created_at}\nStatus: {ticket.status}\nPriority: {ticket.priority}\nDescription: {ticket.description}"
    print(s)

def set_params(params):
    print("Status (Leave blank if none):")
    status = input()
    if status:
         params["status"] = status
    date = r"\d{2}/\d{2}/\d{4}"
    while True:
        print("I want tickets from after (MM/DD/YYYY):")
        after = input()
        if not after:
            break
        if re.match(date, after):
            params["after"] = after
            break
        print("Invalid format")
    while True:
        print("I want tickets from before (MM/DD/YYYY):")
        before = input()
        if not before:
            break
        if re.match(date, before):
            params["before"] = before
            break
        print("Invalid format")
    while True:
        print("Sort by (id, created_by, subject):")
        valid = {"created_at", "id", "subject"}
        sort_by = input()
        if not sort_by:
            break
        if sort_by in valid:
            params["sort_by"] = sort_by
            break
    return params

start()