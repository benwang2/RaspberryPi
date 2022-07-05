from Keycodes import *

null_char = chr(0)

def __write_report__(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def press_key(key: str or int):
    if key in key_map:
        __write_report__(null_char*2 + chr(key_map[key]) + null_char*5)
    elif key in key_map_shifted:
        # shifted key
        __write_report__(chr(32) + null_char + chr(key_map_shifted[key]) +null_char*5)
    
def press_and_release_key(key: str or int):
    press_key(key)
    release_key()

def release_key():
    __write_report__(null_char*8)

def write_string(string: str):
    for char in string:
        press_and_release_key(char)