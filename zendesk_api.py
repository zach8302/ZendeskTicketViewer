import requests

def list_tickets(payload={}):
    r = requests.get('https://zcczach8302.zendesk.com/api/v2/tickets.json', auth=("zach8302@berkeley.edu/token","GBI6JDyDoYw7968zxIn2rYkzc6bjHk5ZZEte0B7N"), params=payload)
    if r.status_code == 200:
        return r.json()
    else:
        return r.status_code

def show_ticket(id):
    r = requests.get(f'https://zcczach8302.zendesk.com/api/v2/tickets/{id}.json', auth=("zach8302@berkeley.edu/token","GBI6JDyDoYw7968zxIn2rYkzc6bjHk5ZZEte0B7N"))
    if r.status_code == 200:
        return r.json()
    else:
        return r.status_code
