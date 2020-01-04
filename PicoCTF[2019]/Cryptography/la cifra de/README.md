# la cifra de

Points: 200
Category: Cryptography

## Problem Statement
>  I found this cipher in an old book. Can you figure out what it says? Connect with nc 2019shell1.picoctf.com 32203. 

## Hints
>  There are tools that make this easy.
>  Perhaps looking at history will help
	
## Solutions 

Let's connect with this address through netcat (nc).

''' console 
nc 2019shell1.picoctf.com 32203
'''

![nc Output](https://i.imgur.com/iwis3mf.png)

It looks like a [Cipher Vigenère](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), for decrypt a Vigenère Cipher 
we need a key but unfortunately we don't have one.

But we know a really [good website](https://www.guballa.de/vigenere-solver) that can decrypt without the key. 
![Website](https://i.imgur.com/24xLPKg.png)

![Decrypter Output](https://i.imgur.com/EpXiRXZ.png)

Perfect! Know we have the text decrypted,key for decryption and the flag!!


## Flag 

`picoCTF{b311a50_0r_v1gn3r3_c1ph3r54ddc1b9}`

-Vex