from zendesk_api import list_tickets, show_ticket
from collections import defaultdict

#The class representing a Zendesk ticket
class Ticket():
    def __init__(self, id, url, status, priority, subject, description, created_at):
        self.id = id
        self.url = url
        self.status = status
        self.priority = priority
        self.subject = subject
        self.description = description
        self.created_at = created_at

    #String representation of a ticket
    def __str__(self):
        return f"[{self.id}] Created: {self.created_at} Status: {self.status} Subject: {self.subject}"

    #Compare the creation date of a ticket with another date
    #Returns: 1 if created after date, 0 if same, -1 if created before date
    def dateCompare(self, date):
        num1 = int(self.created_at[0:4] + self.created_at[5:7] + self.created_at[8:10])
        num2 = int(date[6:10]+ date[0:2] + date[3:5])
        if num1 > num2:
            return 1
        elif num1 == num2:
            return 0
        else:
            return -1

#Gets all tickets with specified parameters
def get_tickets(params):
    payload = {}
    if "sort_by" in params:
        payload["sort_by"] = params["sort_by"]
    tickets_raw = list_tickets(payload)
    if isinstance(tickets_raw, int):
        handle_error(tickets_raw)
        return
    tickets = parse_raw_list(tickets_raw['tickets'])
    return filter_tickets(tickets, params["status"], params["before"], params["after"])
    
#Gets a ticket with a specific id
def get_ticket(id):
    ticket_raw = show_ticket(id)
    if isinstance(ticket_raw, int):
        handle_error(ticket_raw)
        return
    return parse_raw(ticket_raw['ticket'])

#Converts json tickets into instances of Ticket class
def parse_raw_list(lst):
    tickets = []
    for data in lst:
        ticket = parse_raw(data)
        tickets.append(ticket)
    return tickets

#Converts json ticket into an instance of theTicket class
def parse_raw(data):
    id = data['id']
    url = data['url']
    status = data['status']
    priority = data['priority']
    subject = data['subject']
    description = data['description']
    created_at = data["created_at"]
    return Ticket(id, url, status, priority, subject, description, created_at)

#Filters out tickets that do not meet search parameters
def filter_tickets(tickets, status, before, after):
    filtered = []
    for ticket in tickets:
        if (not status or status == ticket.status) and (not before or ticket.dateCompare(before) == -1) and (not after or ticket.dateCompare(after) == 1):
            filtered.append(ticket)
    return filtered

def handle_error(status):
    if status == 401:
        print("[401] Failed to authenticate. Please try again later")
        exit(401)
    elif status == 404:
        return
    else:
        print("Failed to connect to the Zendesk API")
        exit()
