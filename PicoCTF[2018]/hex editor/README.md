# hex editor 

Points: 150

## Problem statement
>  This [cat](https://2018shell.picoctf.com/static/e1230cc4fc0b9b6d8fa6da0b4b918b4f/hex_editor.jpg) has a secret to teach you. You can also find the file in /problems/hex-editor_0_8c20f979e6b2740dee597871ff1a74ee on the shell server. 

## Hints
>  What is a hex editor?
>  Maybe google knows.
>  xxd
>  hexedit
>  bvi

## Solution

Download the image, after that we can use two commands.
Grep and xxd. Grep searchs for a pattern inside a file and xxd creates a hex dump of a given file.

so we type: `grep PicoCTF | xxd hex_editor.jpg`
 

![Output](https://i.imgur.com/yBLrmBSl.png)


## Flag

`picoCTF{and_thats_how_u_edit_hex__kittos_3E03e57d}`

-Vex	
