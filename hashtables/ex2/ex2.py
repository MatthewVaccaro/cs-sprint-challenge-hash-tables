#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create the expected array to be returned
    current = [ticket for ticket in tickets if ticket.source == "NONE"]
    results = [current[0].destination]
    while len(tickets) > 0:

        for ticket in tickets:
            if len(tickets) == 1:
                results.append(ticket.destination)

            if current[0].destination == ticket.source:
                results.append(ticket.destination)
                current = [ticket]
                tickets.remove(ticket)
    
    print("----------", results)
    return results


    # If true append to array
    # Return array current
