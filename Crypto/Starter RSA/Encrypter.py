from Crypto.Util.number import bytes_to_long , getPrime
with open("flag.txt","r") as wow:
    flag = wow.read().strip()
p = getPrime(512)
q = getPrime(512)
n = p* q
e= 65537
q= q + 8*p
leak= -q + 13*p

m = bytes_to_long(flag.encode("utf-8"))
ct = pow(m,e,n)

filed = open("output.txt" , "w")
filed.write("n = " + str(n) + '\n')
filed.write("ct = " + str(ct) + '\n')
filed.write("leak = " + str(leak))
filed.close()