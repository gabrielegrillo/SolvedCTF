# Forensics Warmup 2

Points: 50

## Problem Statement
>  Hmm for some reason I can't open this [PNG](https://2018shell.picoctf.com/static/032d65124629e45f0b5151aad4e7b5b1/flag.png)? Any ideas? 

## Hints
>  How do operating systems know what kind of file it is? (It's not just the ending!
>  Make sure to submit the flag as picoCTF{XXXXX}

## Solutions 

The probelm statement says that this is a PNG file, let's check it using the command file.
File is used to determine the type of a file. 

'file flag.png'

![Output](https://imgur.com/SBw2vRVl.png)

Ok, now we know that it isn't a PNG file but a JPEG. Let's rename it with the right extension.

'mv flag.png flag.jpg'

Wonderful, now we can open the image and we've found the flag!

![Image_Flag](https://imgur.com/8niEQ9Jl.png)

## Flag 

`picoCTF{extensions_are_a_lie}`

-Vex