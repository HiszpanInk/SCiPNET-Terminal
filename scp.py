import time
print("Witaj w bezpośrednim terminalu SCiPNET")
print("Wprowadź proszę komendę")
turnoff = "False"
accessLevel = 0
log = 0
logIn = False
def login():
    print("Użyj proszę swojego poświadczenia")
    poswiadczenie = str(input(""))
    if poswiadczenie == "root | toor":
        print("Poświadczenie Przyjęto")
        log = 1
        accessLevel = 5
def logTest():
    print(log)
def dostep():
    if log is 3:
        print("Odmowa Dostępu")
    else:
        print("Wprowadź indentyfikator obiektu")
        id = str(input(" "))
        file = open(id + ".txt", "r+")
        print(file.read())


while True:
    komenda = input("[SCP]> ")
    if komenda == 'test':
        print(komenda)
    elif komenda == 'login':
        login()
    elif komenda == 'zamknij':
        print("Fundacja SCP 2019")
        time.sleep(1)
        print("zamykanie")
        break
    elif komenda == 'dostep':
        dostep()