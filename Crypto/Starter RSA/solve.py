import sympy as sp
from Crypto.Util.number import long_to_bytes

n = "Value"
ct = "Value"
leak = "Value"
p= sp.Symbol('p')
p = int(max(sp.solve(5*p**2 - leak * p -n  , p)))
print(p)
q = n//p
phi = (p-1)*(q-1)
e = 65537
d = sp.mod_inverse(e,phi)
print(d)
m = pow(ct,d,n)
print(long_to_bytes(m))

##IDEA
"""
n=p*q
q= q + 8*p
leak = -q  +  13*p
leak = -q -8*p + 13*p
leak = -q + 5*p
leak = -n/p + 5*p
leak*p = -n + 5*p^2

5*p^2 -leak *p -n =0

n = p*q
q= n//p
"""