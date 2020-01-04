#!/usr/bin/python3

n = bin(42) #  N equals to the binary value of 42

final = "picoCTF{" + n.replace('0b','') + "}" #  makes the flag ready for copy and paste

print(final)
