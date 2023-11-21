from Crypto.Util.number import *
n = 920139713
p = 18443
q = 49891
e = 19
phi = (q - 1) * (p - 1)
d = inverse(e, phi)
with open('output.txt','r') as f:
  list=f.readlines()
for i in range(len(list)):
  list[i]=int(list[i])
  massage=long_to_bytes(pow(list[i],d,n))
  print(massage.decode(),end='')
