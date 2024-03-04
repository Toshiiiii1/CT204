# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from tkinter import *
from Crypto.Cipher import DES
import base64

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf-8")
    key = pad(keytxt.get()).encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)
    
def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(keytxt.get()).encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    ogtxt.delete(0, END)
    ogtxt.insert(INSERT, detxt)

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb3 = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb3.grid(column=0, row=3)

plaintxt = Entry(window,width=100)
plaintxt.grid(column=1, row=3)
    
keylb4 = Label(window, text="Khóa",font=("Arial", 14))
keylb4.grid(column=0, row=4)

keytxt = Entry(window,width=100)
keytxt.grid(column=1, row=4)

cipherlb5 = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb5.grid(column=0, row=5)

ciphertxt = Entry(window,width=100)
ciphertxt.grid(column=1, row=5)
    
cipherlb6 = Label(window, text="Văn bản được giải hóa",font=("Arial", 14))
cipherlb6.grid(column=0, row=6)

ogtxt = Entry(window,width=100)
ogtxt.grid(column=1, row=6)

encode_btn = Button(window, text="Mã Hóa", command=mahoa_DES)
encode_btn.grid(column=0, row=7)

decode_btn = Button(window, text="Giải mã", command=giaima_DES)
decode_btn.grid(column=1, row=7)

window.geometry('900x600')
window.mainloop()
