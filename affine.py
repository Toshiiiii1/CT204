from math import gcd
from string import ascii_lowercase, ascii_uppercase
import streamlit as st

# Note:
#     - Tải thư viện Streamlit: pip install streamlit
#     - Chạy chương trình: python -m streamlit run affine.py


low_alphabet = ascii_lowercase
up_alphabet = ascii_uppercase

# thuật toán Euclid mở rộng
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = gcd_extended(b % a, a)
        return g, y - (b // a) * x, x

# tính modulo nghịch đảo
def mod_inverse(a, m):
    g, x, y = gcd_extended(a, m)
    return x % m

# kiểm tra 2 số nguyên tố cùng nhau
def check_coprime(a, b):
    return True if gcd(a, b) == 1 else False

# mã hóa
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
    neg_a = mod_inverse(a, m)
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

def main():
    m = 26 # số lượng ký tự
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Nhập số a", step=1, value=2, min_value=2)
    with col2:
        b = st.number_input("Nhập số b", step=1)
        
    if check_coprime(a, m) is True:
        text = st.text_input("Nhập chuỗi cần mã hóa")
        text_encoded = encode(text, a, b, m)
        st.write(f"Chuỗi đã được mã hóa: {text_encoded}")
        
        if st.button("Giải mã", use_container_width=True, type="primary"):
            text_decoded = decode(text_encoded, a, b, m)
            st.write(f"Chuỗi đã ban đầu: {text_decoded}")
        
    else:
        st.warning(f'Hai số {a} và {m} không phải là số nguyên tố cùng nhau', icon="⚠️")

if __name__ == "__main__":
    main()