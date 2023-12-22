from multiprocessing import Process
import os
import time
import pixelsort as pxs
from PIL import Image
i = 0
dat = [0]*5
img = Image.open('1_wm.png')
def f(name, i):
    sorted = pxs.pixelsort(img, randomness=i*10)
    sorted.show()
    print(i)
    
def fm():
    if __name__ == '__main__':
        
        for i in range(3):
            p = Process(target=f, args=('bob',i))
            p.start()
        p.join()

fm()