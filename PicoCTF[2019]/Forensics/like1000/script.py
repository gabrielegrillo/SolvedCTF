import tarfile
import os

for tarnum in range(1000, 0, -1):
     nomfile = str(tarnum) + '.tar'
     file = tarfile.open(nomfile)
     file.extractall()
     print("Done file: {0} ".format(nomfile))
     file.close()

os.system('rm *.tar filler.txt')
os.system('ristretto flag.png')

