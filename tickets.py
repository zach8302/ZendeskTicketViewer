class Ticket():
    def __init__(self, id, priority, subject, description):
        self.id = id
        self.priority = priority
        self.subject = subject
        self.description = description
    def __str__(self):
        return f"[{self.id}] {self.subject}"