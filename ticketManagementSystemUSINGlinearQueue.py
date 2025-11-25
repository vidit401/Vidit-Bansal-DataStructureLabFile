class TicketSystem:
    def __init__(self):
        self.queue = []

    def add_ticket(self, name):
        self.queue.append(name)

    def process_ticket(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "No tickets to process"

    def show_queue(self):
        return self.queue

system = TicketSystem()

while True:
    print("\n-------------------------")
    print("1. Take a Ticket")
    print("2. Process Next Ticket")
    print("3. View All Tickets")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name for ticket: ")
        system.add_ticket(name)
    elif choice == "2":
        result = system.process_ticket()
        print("Serving:", result)
    elif choice == "3":
        print("Waiting Line:", system.show_queue())
    elif choice == "4":
        break