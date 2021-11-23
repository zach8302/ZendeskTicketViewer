from zendesk_api import list_tickets, show_ticket

class Ticket():
    def __init__(self, id, url, status, priority, subject, description, created_at):
        self.id = id
        self.url = url
        self.status = status
        self.priority = priority
        self.subject = subject
        self.description = description
        self.created_at = created_at
    def __str__(self):
        return f"[{self.id}] Created: {self.created_at} Subject: {self.subject}"

def get_tickets(params):
    payload = {}
    if "sort_by" in params:
        payload["sort_by"] = params["sort_by"]
    tickets_raw = list_tickets(payload)
    return parse_raw_list(tickets_raw['tickets'], params)
    
def get_ticket(id):
    return parse_raw(show_ticket(id)['ticket'])

def parse_raw_list(lst, params):
    status = ""
    if "status" in params:
        status = params["status"]
    tickets = []
    for data in lst:
        ticket = parse_raw(data, status)
        if ticket:
            tickets.append(ticket)
    return tickets

def parse_raw(data, status=""):
    if status and status != data['status']:
        return None
    id = data['id']
    url = data['url']
    status = data['status']
    priority = data['priority']
    subject = data['subject']
    description = data['description']
    created_at = data["created_at"]
    return Ticket(id, url, status, priority, subject, description, created_at)