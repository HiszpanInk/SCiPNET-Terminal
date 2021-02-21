import urllib.request
from bs4 import BeautifulSoup
import sys

def access(number):
    scpURL = "http://scp-wiki.wikidot.com/scp-" + str(number)
    scpHTML = urllib.request.urlopen(scpURL).read()
    scpText = str(scpHTML)
    #czyszczenie z jakiegoś szajsu niepotrzebnego typu właściwie cały początek strony na przykład
    scpText = scpText.split('<div id="page-content">')[1]
    scpText = scpText.split('<div class="footer-wikiwalk-nav">')[0]
    scpText = scpText.split('<p><strong>', 1)[1]
    scpText = scpText.split('<span style="text-decoration: underline;">Creator Information</span>')[0]

    scpText = scpText.replace('\\n', '\n')
    scpText = scpText.replace('<br />', '\n')
    scpText = scpText.replace('.', '.\n')
    #czyszczenie tekstu ze znaczników hateemel
    scpTextOutput = (BeautifulSoup(scpText, features="html.parser")).get_text()
    return scpTextOutput

def exit():
    sys.exit()
    


"""
#commandSwitch={'access':access(173)}
while True:
    command = input("[SCP]> ")
    if(command == "access"):
        access(173)
    else:
        sys.exit()
"""