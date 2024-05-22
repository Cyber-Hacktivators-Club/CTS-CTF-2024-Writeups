#!/usr/bin/python
with open("/flag.txt" , "r") as wow:
    flag = bytes.fromhex(wow.read().strip().encode('utf-8').hex())

def hash_function(s):
    return s * 256 + (s)**999999

def isEqual(s1,s2):
    if len(s1) != len(s2): 
        return False
    for i in range(len(s1)):
        if hash_function(s1[i] ^ s2[i]) != 0:
            return False
    return True


def main():
    while True:
        try:
            data = bytes.fromhex(input("Enter flag: "))
        except:
            print("Data format is not valid. Try with hex.")
            continue
        if isEqual(flag,data):
            print("Well done. You cracked me like a pro")
            break
        else:
            print("Wrong. Try harder!.")
            
        print()
    
if __name__ == "__main__":
    main()
