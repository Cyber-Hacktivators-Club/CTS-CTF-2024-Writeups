import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from randcrack import RandCrack
from pwn import *

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext


#io = remote('<IP>','<Port>')
io = process('..\dist\File.py')
io.sendline(b'1')
io.sendline(b'624')
io.readuntil(b'[')
arr = (io.readline().strip())
x = b'arr = [' + arr
exec(x)
rc = RandCrack()
for i in range(624):
	rc.submit(arr[i])
num = rc.predict_randint(1,10000000000)
io.sendline(b'2')
io.sendline(str(num).encode())
io.readuntil("Encrypted Flag in hex: ")

ciphertext = bytes.fromhex(io.readline().strip().decode())
print(ciphertext)
for i in range(0,256):
    key = b''
    x = bytes([i])
    for j in range(16):
        key += x
        random.seed(int(x.hex(),16))
        x=random.randbytes(1)
    random.seed(num)
    newkey = int.from_bytes(random.randbytes(16)) ^ int.from_bytes(key)
    newkey = newkey.to_bytes(len(key) , 'big')
    try:
        flag = decrypt(ciphertext,newkey)
        print(flag)
    except:
        continue
