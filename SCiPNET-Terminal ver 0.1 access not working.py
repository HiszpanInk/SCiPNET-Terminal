import time

print("Welcome to SCiPNET direct access terminal. Please enter command")

turnoff = "False"
accessLevel = 0
logIn = False


def login():
    print("Please enter user authentication")
    poswiadczenie = str(input(""))
    if poswiadczenie == "root | toor":
        print("Authentication accepted. Please enter the command")
        logIn = True
        accessLevel = 5


def logTest():
    print(log)


def dostep():
    if logIn == False:
        print("Access Denied")
    else:
        print("")
        id = str(input(" "))
        file = open(id + ".txt", "r+")
        print(file.read())


while True:
    komenda = input("[SCP]> ")
    if komenda == 'test':
        print(komenda)
    elif komenda == 'login':
        login()
    elif komenda == 'shutdown':
        print("SCP Foundation 2019")
        time.sleep(1)
        print("shutting down")
        break
    elif komenda == 'access':
        dostep()
    else:
        print("Incorrect format or unknown command")