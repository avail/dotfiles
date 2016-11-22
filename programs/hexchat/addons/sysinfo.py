import xchat
__module_name__ = "System Info"
__module_version__ = "0.1"
__module_description__ = "Bet you niggas want to have this"

IRC_BOLD =          "\002"
IRC_COLOR =         "\003"
IRC_COLOR_RESET = 	"\017"
IRC_COLOR_REVERSE = "\026"
IRC_HIDDEN =        "\010"
IRC_UNDERLINE =     "\037"
IRC_ITALICS =       "\035"
COLOR_HILIT =		"06"
PREFIX = IRC_BOLD + IRC_COLOR + COLOR_HILIT
SUFFIX = IRC_BOLD + IRC_COLOR_RESET

try:
	from cpuinfo import cpuinfo
except:
	xchat.prnt("You are missing the cpuinfo module.")
	xchat.prnt("Please be a sweetheart and " + IRC_ITALICS + "pip install py-cpuinfo" + IRC_ITALICS)
try:
	import psutil
except:
	xchat.prnt("You are missing the psutil module.")
	xchat.prnt("Please be a sweetheart and " + IRC_ITALICS + "pip install psutil" + IRC_ITALICS)

import platform
import subprocess
import os

DEBUG = 0

def doCommand(text):
	if DEBUG == 1:
		xchat.prnt(text)
	if DEBUG == 0:
		xchat.command("say " + text)

def doError(text):
	xchat.prnt(IRC_BOLD + IRC_COLOR + "04<<ERROR>> " + IRC_BOLD + IRC_COLOR_RESET + IRC_COLOR + "11" + text)


class Info:
	def getOS(self):
		return PREFIX + "[OS] " + SUFFIX + platform.system() + " " + platform.release() + ";"

	def getRAM(self):
		mem = psutil.phymem_usage()
		totalram = (mem.total / 1024) / 1024
		freeram = (mem.free / 1024) / 1024
		return PREFIX + "[RAM] " + SUFFIX + "Total: " + str(totalram) + "MB; Free: " + str(freeram) + "MB;"

	def getHDD(self):
		partitions = psutil.disk_partitions()

	def getCPU(self):
		info = cpuinfo.get_cpu_info()
		return PREFIX + "[CPU] "+ SUFFIX + info['brand'] + ";"

	def getGPU(self):
		return PREFIX + "[GPU] "+ SUFFIX + join(lines) + ";"


def getInfo(word, word_eol, data):
	i = Info()
	doCommand(i.getOS() + " " + i.getRAM() + " " + i.getCPU())


xchat.hook_command("pyinfo",getInfo)

