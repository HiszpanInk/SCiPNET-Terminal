import urllib.request
import sys

number = 173
scpURL = "http://scp-wiki.wikidot.com/scp-" + str(number)
scpHTML = urllib.request.urlopen(scpURL).read()
scpText = str(scpHTML)
scpText = scpText.split('<div id="page-content">')[1]
scpText = scpText.split('<div class="footer-wikiwalk-nav">')[0]
print(scpText)

"""
def access(number):
    scpURL = "http://scp-wiki.wikidot.com/scp-" + str(number)
    scpText = urllib.request.urlopen(scpURL)
    print(scpURL)
    print(str(scpText))
    

def exit():
    sys.exit()
    'run':exit()



#commandSwitch={'access':access(173)}
while True:
    command = input("[SCP]> ")
    if(command == "access"):
        access(173)
    else:
        sys.exit()
"""