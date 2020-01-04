# 2Warm

Points: 50
Category: Binary Exploitation

## Problem Statement
>  How do you execute a program in a command line? 

## Hints
>  You're going to need to know how to run programs if you're going to get out of here. Navigate to /problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e on the shell server and run this program to receive a flag.

## Solutions  

MAKE SURE THAT YOU HAVE INSTALLED THE 32 BITS LIBRARIES! (my mistake ahah) [Link](https://support.humblebundle.com/hc/en-us/articles/202759400-Installazione-di-librerie-a-32-bit-su-un-sistema-Linux-a-64-bit)

Anyway, let's run file run_this for find which type of file is it.

![Output file](https://i.imgur.com/zyRKjc3.png)

Let's make it executable with the command:

'''console 
chmod +x run_this'''

then execute the file.

'''console
./run_this'''

![Flag](https://i.imgur.com/RnJRqg2.png)

## Flag 

`picoCTF{g3t_r3adY_2_r3v3r53}`

-Vex
