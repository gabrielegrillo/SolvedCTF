# grep 1

Points: 75

## Problem Statement
>  Can you find the flag in [file](https://2018shell.picoctf.com/static/d7d1b6b0a64801c499a5eea393224811/file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2 on the shell server. 

## Hints
>  grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solutions 

In this challange you have to use the command grep that searchs for a pattern in a file. 
So we use cat for view the content of the file and grep for find the pattern.

`cat file | grep picoCTF`

![Output](https://imgur.com/Wm8nKFDl.png)

## Flag 

`picoCTF{grep_and_you_will_find_cdf2e7c2}`

-Vex
