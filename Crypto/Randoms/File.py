#!/usr/local/bin/python
import random
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
print("Welcome to my maze that changes everytime")
flag = open('/flag.txt','rb').read().strip()
def menu():
    print("""
          Choose an option:
          1. Get Random Data
          2. Get Flag
          3. Exit """)
    
def second_exists(num):
    random.seed(int(os.urandom(64).hex(),16))
    key = b''
    intermediate = random.randbytes(1)
    for i in range(16):
        key += intermediate
        random.seed(int(intermediate.hex(),16))
        intermediate = random.randbytes(1)
    random.seed(num)
    newkey = int.from_bytes(random.randbytes(16)) ^ int.from_bytes(key)
    newkey = newkey.to_bytes(len(key) , 'big')
    enc_flag = encrypt_flag(flag,newkey)
    print(f"Encrypted Flag in hex: {enc_flag.hex()}")

def encrypt_flag(message,key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

while True:
    menu()
    try:
        data = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if data == 1:
        total = []
        try:
            i = int(input("How many random numbers do you want: "))
        except ValueError:
            continue
        for x in range(i):    
            total.append(random.getrandbits(32))
        print(total)

    elif data == 2:
        print("Not so fast bro, just answer a simple question")
        print("Guess a number which I am thinking from 1-10000000000")
        num = random.randint(1,10000000000)
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess == num:
            print("You guessed right")
            second_exists(num)
            exit()
        else:
            print("You guessed wrong")
            
            exit()
    else:
        
        exit()