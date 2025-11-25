class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()

while True:
    print("\n1. Add Item")
    print("2. Show List")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        val = input("Enter value: ")
        my_list.append(val)
    elif choice == "2":
        my_list.display()
    elif choice == "3":
        break