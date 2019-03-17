import time

class Terminal:
    turnoff = "False"
    accessLevel = 0
    logIn = False

    def login(self):
        print("Please enter user authentication")
        poswiadczenie = str(input(""))
        if poswiadczenie == "root | toor":
            print("Authentication accepted. Please enter the command")
            self.logIn = True
            self.accessLevel = 5

    def dostep(self):
        print("")
        id = str(input("Please enter SCP identificator"))
        file = open(id + ".txt", "r+")
        print(file.read())

    def run(self):
        print("Welcome to SCiPNET direct access terminal. Please enter command")
        while True:
            komenda = input("[SCP]> ")
            if komenda == 'test':
                print(komenda)
            elif komenda == 'login':
                self.login()
            elif komenda == 'shutdown':
                print("SCP Foundation 2019")
                time.sleep(1)
                print("shutting down")
                break
            elif komenda == 'access' and self.logIn:
                self.dostep()
            elif komenda == 'access' and self.logIn == False:
                print("Access Denied")
            else:
                print("Incorrect format or unknown command")



