import requests

def list_tickets():
    r = requests.get('https://zcczach8302.zendesk.com/api/v2/tickets.json', auth=("user","pass"))
    if r.status_code == 200:
        return r.json()
    else:
        return "Error"

def show_ticket(id):
    r = requests.get('https://zcczach8302.zendesk.com/api/v2/tickets/{id}.json', auth=("user","pass"))
    if r.status_code == 200:
        return r.json()
    else:
        return "Error"

def count_tickets():
    r = requests.get('https://zcczach8302.zendesk.com/api/v2/tickets/count.json', auth=("user","pass"))
    if r.status_code == 200:
        return r.json()
    else:
        return "Error"