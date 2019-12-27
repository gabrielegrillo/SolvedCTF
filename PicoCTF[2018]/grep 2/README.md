# grep 2 

Points: 125

## Problem statement
>  This one is a little bit harder. Can you find the flag in /problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files on the shell server? Remember, grep is your friend.

## Hints
>  grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

Go to in the directory: /problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files
tip: use ssh via your terminal and not from the webshell 
As we can see there are a lot of files... and we can't use a single grep command.

But there's a option for use grep recursively:  grep -R pattern

So we type... "grep -R picoCTF"

![Output](https://i.imgur.com/YY0O2LY.png)

in the folder "files5", file "file23" there is the flag!

## Flag

`picoCTF{grep_r_and_you_will_find_24c911ab}`

-Vex	
