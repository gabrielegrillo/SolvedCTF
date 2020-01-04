# First Grep

Points: 100
Category: General Skills

## Problem Statement
>  Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52 on the shell server. 

## Hints
>  grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solutions 

In this challange you have to use the command grep that searchs for a pattern in a file. 
So we use cat for view the content of the file and grep for find the pattern.

```console
cat file | grep picoCTF
```

![Output](https://imgur.com/ldNEhWzl.png)

## Flag 

`picoCTF{grep_is_good_to_find_things_4b2451ea}`

-Vex
