from functions import access
import sys
#I will do it better sometime
while True:
    command = input("[SCP]> ")
    if(command == "access"):
        scpNum = input("Enter ID of SCP you want to access: ")
        print("\n", access(scpNum))
    elif(command == "exit"):
        sys.exit()
    else:
        print("This command does not exist!")    

"""
#commandSwitch={'access':access(173)}
while True:
    command = input("[SCP]> ")
    if(command == "access"):
        access(173)
    else:
        sys.exit()
"""