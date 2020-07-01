# Glory of the Garden 

Points: 50
Category: Forensics

## Problem statement
>  This [garden](https://2019shell1.picoctf.com/static/438c667542717e152254bb4ae9297eb1/garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_3_346e50df4a37bcc4aa5f6e5831604e2a on the shell server.

## Hints
>  What is a hex editor?

## Solution

Download the image, after that we can use two commands.
Grep and xxd. Grep searchs for a pattern inside a file and xxd creates a hex dump of a given file.

so we type: 
'''console 
grep PicoCTF | xxd garden.jpg
'''
 

![Output](https://i.imgur.com/erLyJNZ.png)


## Flag

`picoCTF{more_than_m33ts_the_3y35a97d3bB}`

-Vex	
