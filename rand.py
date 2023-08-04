#dev by sl1ppy
#only eng, encoding break

import random
import os
import time

peremen = 0

print ('\nWrite "go"\n')


if __name__ == '__main__':

    text = 'go'
    proverka = input()

    if len(proverka) == 2 and text in proverka.lower():
        if text in proverka.lower():
            print ('\n\nGood!\n\n')
            peremen = 1 
    else:
        print ('\n\nError!!!\n\n')          

if peremen == 0:
    pass
else:
    time.sleep(1)
    print('One second...')
    time.sleep(random.randint(2, 7))
    peremen = 2

if peremen == 2:
    print ('\n\nDo you agree to play a game to delete a folder from your computer?\n')
    print ('Y - YES')
    print ('N - NO')
    print ('Pliz write in terminal!\n')
    sogl = input()
    if sogl == 'Y':
        print ('\n\n\n\nOK, game starts!\n\n\n\n')
        peremen = 3
    else:
        print ('\n\n\n\nBAD BOY? bb\n\n\n\n')

if peremen == 3:
    crand = 0 
    time.sleep(1)
    print ('\n\n\nLoading...\n\n\n')
    time.sleep(random.randint(5, 10))
    crand = random.randint(1, 5)
    if crand == 3:
        print ('\n\nDelete folder =(\n\n') 
        os.rmdir('D:\project\check') # path
        time.sleep(1)
        print ('\n\ndev by sl1ppy\n\n')
    else:
        print ('\n\n\n\nYou are lucky today!\n\n\n\n')
        time.sleep(1)
        print ('\n\ndev by sl1ppy\n\n')
     
