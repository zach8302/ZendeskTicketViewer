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
    return parse_json(list_tickets())
def get_ticket(id):
    return
def parse_json(raw):
    tickets = []
    for data in raw['tickets']:
        id = data['id']
        priority = data['priority']
        subject = data['status']
        description = data['description']
        t = Ticket(id, priority, subject, description)
        tickets.append(t)
    return tickets


for t in get_tickets():
    print(f"{t}\n")