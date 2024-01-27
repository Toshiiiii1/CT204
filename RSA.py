from sympy import primerange
import random
from math import lcm, gcd

# pip install sympy

# thuật toán Euclid mở rộng
def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_extended(b % a, a)
        return (g, x - (b // a) * y, y)

# tính nghịch đảo modulo
def mod_inverse(a, m):
    g, x, y = gcd_extended(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def generate_key():
    # chọn ngẫu nhiên 2 số nguyên tố p và q
    prime = list(primerange(1000, 2000))
    p, q = random.choice(prime), random.choice(prime)
    n = p * q
    lambda_n = lcm(p-1, q-1)

    # Tìm số e sao cho e và lambda_n nguyên tố cùng nhau
    for e in range(2, lambda_n+1):
        if gcd(e, lambda_n) == 1:
            break
    
    # tính d là nghịch đảo modulo của e
    d = mod_inverse(e, lambda_n)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(plain_text, public_key):
    encoded = []
    # chuyển từng ký tự -> số, mã hóa từng ký tự
    for character in plain_text:
        encoded.append(ord(character)**public_key[1] % public_key[0])
    cipher_text = "".join([str(i) for i in encoded])
    return encoded, cipher_text
 
def decrypt(encoded, private_key):
    seq = ''
    # giải mã từng ký tự
    for num in encoded:
        seq += chr((num**private_key[1]) % private_key[0])
    return seq

def main():
    plain_text = input("Nhap chuoi: ")
    # khởi tạo cặp khóa
    public_key, private_key = generate_key()
    encode, cipher_text = encrypt(plain_text, public_key)
    decode = decrypt(encode, private_key)

    print(cipher_text)
    print(decode)

if __name__ == "__main__":
    main()