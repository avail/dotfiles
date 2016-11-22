import hexchat

__module_name__ = "~blah"
__module_version__ = "0.1"
__module_description__ = "Recreation of NTA's ~blah script"

oldnick = hexchat.get_info("nick")   # we use whatever a person's nick is as
                                     # default when the plugin loads
def doStuff(word, eol, data):
    try:
        suffix = word[1]
        hexchat.command("say ~"+ suffix)
        hexchat.command("nick "+ oldnick +"|"+ suffix)
    except IndexError:
        hexchat.command("say ~")
        hexchat.command("nick "+ oldnick)

hexchat.hook_command("blah", doStuff)