from zendesk_api import list_tickets, show_ticket, count_tickets

class Ticket():
    def __init__(self, id, priority, subject, description):
        self.id = id
        self.priority = priority
        self.subject = subject
        self.description = description
    def __str__(self):
        return f"[{self.id}] {self.subject}"

def get_tickets():
    tickets_raw = list_tickets()
    return parse_raw_list(tickets_raw['tickets'])
    
def get_ticket(id):
    return parse_raw(show_ticket(id)['ticket'])

def parse_raw_list(lst):
    tickets = []
    for data in lst:
        tickets.append(parse_raw(data))
    return tickets

def parse_raw(data):
    id = data['id']
    priority = data['priority']
    subject = data['subject']
    description = data['description']
    return Ticket(id, priority, subject, description)