from Keycodes import *

null_char = chr(0)

def __write_report__(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def press_and_release_key(key: str or int):
    if key in key_map:
        __write_report__(null_char*2 + key + null_char*5)
    else:
        # shifted key
        __write_report__(chr(32) + null_char + key.lower() +null_char*5)

def write_string(string: str):
    for char in string:
        press_and_release_key(char)

