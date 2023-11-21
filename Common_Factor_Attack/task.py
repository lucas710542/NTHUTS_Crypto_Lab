from Crypto.Util.number import *
from secret import flag

p1 = getPrime(128)
p2 = getPrime(128)
p3 = getPrime(128)
n1 = p1 * p2
n2 = p2 * p3
e = 0x1001
m1 = bytes_to_long(flag.encode()[:20])
m2 = bytes_to_long(flag.encode()[20:])
c1 = pow(m1, e, n1)
c2 = pow(m2, e, n2)

with open("output.txt","w") as f:
    f.write(f'n1 = {n1}\nn2 = {n2}\ne = {e}\nc1 = {c1}\nc2 = {c2}\n')
