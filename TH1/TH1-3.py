# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from tkinter import *
from string import ascii_lowercase, ascii_uppercase

low_alphabet = ascii_lowercase
up_alphabet = ascii_uppercase

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

# def Char2Num(c):
#     return ord(c)-65

# def Num2Char(n):
#     return chr(n+65)

# def encryptAF(txt,a,b,m):
#     r = ""
#     for c in txt:
#         e = (a*Char2Num(c)+b) % m
#         r = r+Num2Char(e)
#     return r

# def decryptAF(txt,a,b,m):
#     r = ""
#     a1 = xgcd(a,m)
#     for c in txt:
#         e = (a1*(Char2Num(c)-b )) % m
#         r = r+Num2Char(e)
#     return r

# Bai 3
def encode(text, a, b, m):
    temp = []
    for x in text:
        if x.islower():
            temp.append(low_alphabet[(a*low_alphabet.index(x) + b)%m])
        elif x.isupper():
            temp.append(up_alphabet[(a*up_alphabet.index(x) + b)%m])
        else:
            temp.append(x)
            
    result = "".join(temp)
    return result

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    # entxt = encryptAF(plaintxt.get(), a, b, m)
    entxt = encode(plaintxt.get(), a, b, m)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT ,entxt)

def decode(text, a, b, m):
    neg_a = xgcd(a, m)
    temp = []
    for y in text:
        if y.islower():
            temp.append(low_alphabet[(neg_a*(low_alphabet.index(y) - b))%m])
        elif y.isupper():
            temp.append(up_alphabet[(neg_a*(up_alphabet.index(y) - b))%m])
        else:
            temp.append(y)
    result = "".join(temp)
    return result

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    # detxt = decryptAF(ciphertxt.get(), a, b, m)
    detxt = decode(ciphertxt.get(), a, b, m)
    ogtxt.delete(0, END)
    ogtxt.insert(INSERT, detxt)

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)

plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)

plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)

KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))

KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)

# Hoc vien bo sung code tai day
# de co duoc giao dien nhu yeu cau
cipherlb5 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
cipherlb5.grid(column=0, row=4)

ciphertxt = Entry(window,width=20)
ciphertxt.grid(column=1, row=4)

ogtxt = Entry(window,width=20)
ogtxt.grid(column=3, row=4)


# Tao nut co ten AFbtn
AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)

# Hoc vien bo sung code de tao nut co ten la DEAFbtn
AFbtn = Button(window, text="Giải mã", command=giaima)
AFbtn.grid(column=2, row=4)

# Hien thi cua so
window.geometry('800x600')
window.mainloop()
