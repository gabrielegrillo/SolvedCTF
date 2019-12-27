#!/usr/bin/python3

n = bin(27)
final = "picoCTF{" + n.replace('0b','') + "}" 
print(final)
