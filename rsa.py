import math
p = 13
q = 17
phi = (p-1) * (q-1)
e = 35
d = math.gcd(phi, e)
while d != 1:
 e = e + phi
 d = math.gcd(phi, e)
private_key = e % phi
print("Private key:", private_key)
