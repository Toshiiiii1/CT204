# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

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

# def encryptAF(txt, a, b, m):
#     r = ""
#     for c in txt:
#         e = (a*Char2Num(c)+b) % m
#         r = r+Num2Char(e)
#     return r

# def decryptAF(txt, a, b, m):
#     r = ""
#     a1 = xgcd(a,m)
#     for c in txt:
#         e = (a1*(Char2Num(c)-b )) % m
#         r = r+Num2Char(e)
#     return r

# Bai 2
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

# giải mã
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


a, b, m = 3, 5, 26
plain_text = "HELLO"
cipher_text = encode(plain_text, a, b, m)
og_text = decode(cipher_text, a, b, m)
print(f"Cipher text: {cipher_text}")
print(f"Plain text: {og_text}")