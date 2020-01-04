# like1000

Points: 250
Category: Forensics

## Problem statement
>  This [.tar](https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar) file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

## Hints
>  Try and script this, it'll save you alot of time

## Solution

Download the file with the command:

```console 
wget --no-check-certificate https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar
```


![Download the tar](https://i.imgur.com/2cvHaIj.png)


Then you can make your own script or use mine.

```python3
import tarfile
import os


for tarnum in range(1000, 0, -1):
     nomfile = str(tarnum) + '.tar'
     file = tarfile.open(nomfile)
     file.extractall()
     print("Done file: {0} ".format(nomfile))
     file.close()

os.system('rm *.tar filler.txt')
os.system('ristretto flag.png') # ristretto is my image viewer for the Xfce desktop. 
```


![Output ristretto flag.png](https://i.imgur.com/o6Xmwf7.png)


## Flag

`picoCTF{l0t5_0f_TAR5}`

-Vex	
