from typing import Type
import unittest
from tickets import *
from collections import defaultdict

class TestTicket(unittest.TestCase):

    def test_get_all_tickets(self):
        params = defaultdict(lambda: None)
        tickets = get_tickets(params)
        self.assertGreater(len(tickets), 0)
        test_ticket = Ticket(123, "test.com", "open", "high", "test", "hello world", "2021-11-22T18:29:52Z")
        for ticket in tickets:
            self.assertEqual(type(ticket), type(test_ticket))

    def test_select_ticket(self):
        ticket = get_ticket(5)
        test_ticket = Ticket(123, "test.com", "open", "high", "test", "hello world", "2021-11-22T18:29:52Z")
        self.assertEqual(type(ticket), type(test_ticket))

    def test_invalid_select(self):
        ticket = get_ticket(-239)
        self.assertIsNone(ticket)

    def test_date_comp(self):
        ticket = Ticket(123, "test.com", "open", "high", "test", "hello world", "2021-11-22T18:29:52Z")
        before = "02/21/2013"
        same = "11/22/2021"
        after = "11/23/2021"
        self.assertEqual(ticket.dateCompare(before), 1)
        self.assertEqual(ticket.dateCompare(same), 0)
        self.assertEqual(ticket.dateCompare(after), -1)

class TestParams(unittest.TestCase):

    def test_status(self):
        params = defaultdict(lambda: None)

        params["status"] = "open"
        for ticket in get_tickets(params):
            self.assertEqual(ticket.status, "open")

        params["status"] = "pending"
        for ticket in get_tickets(params):
            self.assertEqual(ticket.status, "pending")

        params["status"] = "closed"
        for ticket in get_tickets(params):
            self.assertEqual(ticket.status, "closed")
    
    def test_before(self):
        params = defaultdict(lambda: None)

        params["before"] = "11/24/2021"
        for ticket in get_tickets(params):
            self.assertEqual(ticket.dateCompare("11/24/2021"), -1)
    
    def test_after(self):
        params = defaultdict(lambda: None)

        params["after"] = "11/23/2021"
        for ticket in get_tickets(params):
            self.assertEqual(ticket.dateCompare("11/23/2021"), 1)
    
    def test_no_matches(self):
        params = defaultdict(lambda: None)
        params["status"] = "open"
        params["before"] = "12/19/1999"
        tickets = get_tickets(params)
        self.assertEqual(len(tickets), 0)

if __name__ == '__main__':
    unittest.main()