class Browser:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url):
        self.history = self.history[0 : self.current_index + 1]
        self.history.append(url)
        self.current_index += 1
        return self.history[self.current_index]

    def back(self, steps):
        self.current_index -= steps
        if self.current_index < 0:
            self.current_index = 0
        return self.history[self.current_index]

    def forward(self, steps):
        self.current_index += steps
        if self.current_index >= len(self.history):
            self.current_index = len(self.history) - 1
        return self.history[self.current_index]

browser = Browser("google.com")

while True:
    print("\n-------------------------")
    print("Current Page:", browser.history[browser.current_index])
    print("-------------------------")
    print("1. Visit a new URL")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        site = input("Enter website name: ")
        browser.visit(site)
    elif choice == "2":
        steps = int(input("How many steps back? "))
        browser.back(steps)
    elif choice == "3":
        steps = int(input("How many steps forward? "))
        browser.forward(steps)
    elif choice == "4":
        break