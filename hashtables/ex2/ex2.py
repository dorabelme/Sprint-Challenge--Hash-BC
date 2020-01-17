#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import HashTable
from hashtables import hash_table_insert
from hashtables import hash_table_retrieve


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
       hash_table_insert(hashtable, ticket.source, ticket.destination)

    location = hash_table_retrieve(hashtable, "NONE")

    for i in range(length):
        route[i] = location
        location = hash_table_retrieve(hashtable, location)

    return route