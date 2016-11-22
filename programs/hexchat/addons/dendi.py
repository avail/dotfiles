import xchat, urllib2
from bs4 import BeautifulSoup

__module_name__ = "slash dendi"
__module_version__ = "1.0.0"
__module_description__ = "Pukes out a random Dendi fact each time"

def dendi(word, word_eol, data):
    request = urllib2.Request("http://dendifacts.com", headers={"User-Agent": "Dendi Facts"})
    content = urllib2.urlopen(request).read()
    soup = BeautifulSoup(content, "html.parser")
    xchat.command("say "+ soup.find_all('p', attrs={"id": "quote-fact"})[0].text.encode('utf-8').strip())
    xchat.EAT_ALL

xchat.hook_command("dendi",dendi)