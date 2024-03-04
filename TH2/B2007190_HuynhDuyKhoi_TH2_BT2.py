# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from tkinter import *
from Crypto.Cipher import DES
import base64
from string import ascii_uppercase, digits
import random

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES(plaintxt, keytxt):
    txt = pad(plaintxt).encode("utf-8")
    key = pad(keytxt).encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    
    return entxt
    
def giaima_DES(ciphertxt, keytxt):
    txt = ciphertxt
    txt = base64.b64decode(txt)
    key = pad(keytxt).encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))

    return detxt

def generate_key():
    key = ""
    for _ in range(7):
        key += random.choice(ascii_uppercase + digits)
    return key
    
with open("./text.txt", "r+") as file:
    plaintxt = file.readline()

    keytxt = generate_key()

    ciphertxt = mahoa_DES(plaintxt, keytxt)

    file.write(f"\nCipher text: {ciphertxt.decode('utf-8')}")

    ogtxt = giaima_DES(ciphertxt, keytxt)

    file.write(f"\nPlain text: {ogtxt.decode('utf-8')}")
    file.close()