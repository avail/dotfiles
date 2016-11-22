import sys, re, xchat, base64, time, random, urllib2
from time import localtime, strftime
from bs4 import BeautifulSoup

__module_name__ = "Useful Stuff"
__module_version__ = "0.1"
__module_description__ = "NP, Time and Encode/Decode Plugin"

IRC_BOLD =           "\002"
IRC_COLOR =          "\003"
IRC_COLOR_RESET =    "\017"
IRC_COLOR_REVERSE =  "\026"
IRC_HIDDEN =         "\010"
IRC_UNDERLINE =      "\037"
IRC_ITALICS =        "\035"

DEBUG = 0

def doCommand(text):
    if DEBUG == 1:
        xchat.prnt(text)
    if DEBUG == 0:
            xchat.command(text)
    xchat.EAT_ALL

def doError(text):
    xchat.prnt(IRC_BOLD + IRC_COLOR + "04<<ERROR>> " + IRC_BOLD + IRC_COLOR_RESET + IRC_COLOR + "11" + text)

def doB64Decode(word, word_eol, data):
    page = base64.b64decode(word_eol[1])
    xchat.prnt("Decoded string: " + page)


def doB64Encode(word, word_eol, data):
    page = base64.b64encode(word_eol[1])
    xchat.prnt("Encoded string: " + page)
    # xchat.command("say " + page)

def doTime(word, eol, data):
    # default to format 12 hour format
    try:
        if word[1] == "12":
            doCommand('action current time: ' + strftime("%I:%M:%S %p", localtime())) #12 hour
        elif word[1] == "24":
            doCommand('action current time: ' + strftime("%H:%M:%S", localtime()).lstrip('0')) #24 hour
        return xchat.EAT_ALL # kills remaining bits of memory
    except IndexError:
        doError("No time format specified (12/24), defaulting to 24.")
        doCommand('action current time: ' + strftime("%H:%M:%S", localtime()).lstrip('0')) #24 hour

def doNP(word,eol,data):
    try:
        path = open("%userprofile%\\Documents\\CurrentTrackInfo.txt", "r")
        out = path.read()
        doCommand("me is now playing: " + out + " ")
    except IOError:
        doError("AIMP is not running")

def doRainbow(word, word_eol, data):
    try:
        tostr = ""
        for element in list(word_eol[1].decode('utf-8')):

            color = random.randint(2,13)

            if color < 10:
                color = "0" + str(color)

            tostr += "\003" + str(color) + element

        doCommand("say " + tostr.encode('utf-8'))
    except IndexError:
        doError("No text specified. Syntax: /rainbow [text here]")

def doDots(word, word_eol, data):
    colors = [10, 11, 12, 2, 6, 13, 4, 7, 8, 9, 3]
    dot = u"\u2764" # heart=u2764 #dot = u25cf
    ret = ""
    for letter in list(word_eol[1].decode('utf-8')):
        ret += "\003" + str(random.choice(colors)) + ",1" + dot + "\003\0030,1" + letter + "\003"
    ret += "\003" + str(random.choice(colors)) + ",1" + dot + "\003"
    doCommand("say "+ ret.encode('utf-8'))

def dendi(word, word_eol, data):
    request = urllib2.Request("http://dendifacts.com", headers={"User-Agent": "Dendi Facts"})
    content = urllib2.urlopen(request).read()
    soup = BeautifulSoup(content, "html.parser")
    for rows in soup.find_all('p', attrs={"id": "quote-fact"}):
        doCommand("say "+ rows.text.encode('utf-8').strip())


xchat.hook_command("rainbow",doRainbow)
xchat.hook_command("np",doNP)
xchat.hook_command("time",doTime)
xchat.hook_command("decode",doB64Decode)
xchat.hook_command("encode",doB64Encode)
xchat.hook_command("dots",doDots)
xchat.hook_command("dendi",dendi)