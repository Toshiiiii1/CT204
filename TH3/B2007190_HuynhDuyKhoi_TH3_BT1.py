# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog
from Crypto.Random import get_random_bytes

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(
        mode = _mode,
        initialdir = "D:\Code\Python Code\CT204\TH3\U",
        title = _title,
        filetypes = _filetypes,
        defaultextension = _defaultextension
    )
    if f is None: return
    f.write(content)
    f.close()

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(
        key.exportKey('PEM'),
        'wb',
        'Lưu khóa cá nhân',
        (("All files", "*.*"), ("PEM files", "*.pem")),
        ".pem"
    )
    pub = save_file(
        key.publickey().exportKey('PEM'),
        'wb',
        'Lưu khóa công khai',
        (("All files", "*.*"),("PEM files", "*.pem")),
        ".pem"
    )
    pri_key.delete(0, END)
    pri_key.insert(END,key.exportKey('PEM'))
    pub_key.delete(0 ,END)
    pub_key.insert(END,key.publickey().exportKey('PEM'))
    
def get_key(key_style):
    filename = filedialog.askopenfilename(
        initialdir = "D:\Code\Python Code\CT204\TH3",
        title = "Open " + key_style,
        filetypes = (("PEM files", "*.pem"),
        ("All files", "*.*"))
    )
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)
    
def giaima_rsa():
    sentinel = get_random_bytes(1024)
    txt = ciphertxt.get().encode()
    pri_key = get_key("Private Key")
    cipher = PKCS1_v1_5.new(pri_key)
    txt = base64.b64decode(txt)
    detxt = cipher.decrypt(txt, sentinel).decode()
    ogtxt.delete(0,END)
    ogtxt.insert(INSERT,detxt)

window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ BẤT ĐỐI XỨNG RSA", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb3 = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb3.grid(column=0, row=3)

plaintxt = Entry(window,width=100)
plaintxt.grid(column=1, row=3)

cipherlb4 = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb4.grid(column=0, row=4)

ciphertxt = Entry(window,width=100)
ciphertxt.grid(column=1, row=4)

plaintextlb5 = Label(window, text="Văn bản được giải hóa",font=("Arial", 14))
plaintextlb5.grid(column=0, row=5)

ogtxt = Entry(window,width=100)
ogtxt.grid(column=1, row=5)
    
prikeylb6 = Label(window, text="Khóa cá nhân",font=("Arial", 14))
prikeylb6.grid(column=0, row=6)

pri_key = Entry(window, width=100)
pri_key.grid(column=1, row=6)

pubkeylb7 = Label(window, text="Khóa công khai",font=("Arial", 14))
pubkeylb7.grid(column=0, row=7)

pub_key = Entry(window, width=100)
pub_key.grid(column=1, row=7)

gen_key_btn = Button(window, text="Tạo khóa", command=generate_key)
gen_key_btn.grid(column=1, row=8)

encode_btn = Button(window, text="Mã Hóa", command=mahoa_rsa)
encode_btn.grid(column=1, row=9)

decode_btn = Button(window, text="Giải mã", command=giaima_rsa)
decode_btn.grid(column=1, row=10)

window.geometry('900x600')
window.mainloop()
