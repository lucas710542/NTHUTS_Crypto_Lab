from Crypto.Util.number import *
from secret import flag

n = 920139713
e = 19

cipher_list = []
for i in flag:
    m_int = bytes_to_long(i.encode())
    cipher_list.append(str(pow(m_int, e, n)))

with open("output.txt", "w") as f:
    for cipher in cipher_list:
        f.write(cipher + '\n')
