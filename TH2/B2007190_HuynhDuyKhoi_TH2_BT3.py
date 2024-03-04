# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from tkinter import *
from Crypto.Cipher import DES
import base64
from string import ascii_uppercase, digits
import random
import pandas as pd

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
    
keys = pd.read_csv("./country.csv")

# lọc ra những key đủ 8 bytes
keys['word_count'] = keys['value'].apply(lambda x: len(str(x)))
keys = keys[keys['word_count'] < 7]
keys = keys.drop(columns=["word_count"])


cipher_text1 = "lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=="

cipher_text2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="

cipher_text3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"

plain_txt1 = "The treasure is under the coconut tree"

for key in keys["value"]:
    temp = giaima_DES(cipher_text1.encode("utf-8"), key)
    if plain_txt1.encode("utf-8") == temp:
        print(f"Key: {key}")
        break
    
print(f"Plain text 2: {giaima_DES(cipher_text2, key).decode('utf-8')}")
print(f"Plain text 3: {giaima_DES(cipher_text3, key).decode('utf-8')}")