disclaimer='''
DDDD    I    SSS     CCC   L       AAA    I   MM   MM   EEEE   RRRR
D   D       S       C      L      A   A       M M M M   E      R   R
D   D   I    SSS    C      L      AAAAA   I   M  M  M   EEEE   RRRR
D   D   I       S   C      L      A   A   I   M     M   E      R   R
DDDD    I    SSS     CCC   LLLL   A   A   I   M     M   EEEE   R   R



           ! This iDOR can withdraw unavailable fics !
           
           
           
'''
print(disclaimer)
bef='https://ficbook.net/readfic/'
import random
import requests
import sys
import os
from sys import platform
try:
    while True:
        number = random.randrange(1, 9999999)
        numbert = str(number)
        r = requests.get(bef+numbert)
        if r.status_code == 200:
            print('Fic exist: '+bef+numbert)
            with open('existfics.txt', 'a') as existfics:
                existfics.write(bef+numbert)
except KeyboardInterrupt:
    if platform == "linux" or platform == "linux2" or platform == "Linux" or platform == "darwin" or platform == "Darwin":
        os.system("clear")
    else:
        os.system("cls")
    exit("Ctrl-C'd")
