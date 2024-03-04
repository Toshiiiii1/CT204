# Ho va ten sinh vien: Huynh Duy Khoi
# Ma so sinh vien: B2007190
# STT: 7

from string import ascii_lowercase, ascii_uppercase

low_alphabet = ascii_lowercase
up_alphabet = ascii_uppercase

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

# Bai 1
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

print(encode("HELLO", 3, 5, 26))
