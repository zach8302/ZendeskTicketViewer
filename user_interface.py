from tickets import *

def start():
    commands = {"view":view_tickets, "select":view_ticket, "params":set_params}
    params = {}
    print("Zendesk Ticket Viewer\nTo view all tickets enter: view\nTo view a specific ticket enter: select")
    while True:
        print("Enter a Command:")
        command = input()
        if command in commands:
            commands[command](params)



def view_tickets(params):
    tickets = get_tickets(params)
    num = len(tickets)
    if num > 25:
        i = 0
        while i < num:
            print(f"Showing Tickets {i + 1} through {i + 25} of {num}")
            for t in tickets[i:i+25]:
                print(t)
            command = input()
            if command == "next":
                i += 25
            elif command == "exit":
                break
    else:
        for t in tickets:
            print(t)

def view_ticket(params):
    id = input()
    ticket = get_ticket(id)
    s = f"\n{ticket.url}\n[{ticket.id}]\nSubject: {ticket.subject}\nCreated: {ticket.created_at}\nStatus: {ticket.status}\nPriority: {ticket.priority}\nDescription: {ticket.description}"
    print(s)

def set_params(params):
    # status = input()
    # if status:
    #     params["status"] = status
    # while True:
    #     before = input()
    #     if not before:
    #         break
    #     params["before"] = before
    # while True:
    #     after = input()
    #     if not after:
    #         break
    #     params["after"] = after
    while True:
        valid = {"created_at", "id", "subject"}
        sort_by = input()
        if sort_by in valid:
            params["sort_by"] = sort_by
            break
    return params

    



start()