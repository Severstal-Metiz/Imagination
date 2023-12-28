from pixelsort import pixelsort
import ffmpeg
import os
import time
from PIL import Image
import PIL

import multiprocessing as mp

temppath = 'temp/'




def pixsort(sorting_function, interval_function, angle, clength, interval_image, randomness, i):
    img = Image.open('input.png')

    output_img = pixelsort(img, sorting_function=sorting_function,
                           interval_function=interval_function, randomness=randomness, angle=angle, clength=clength,
                           interval_image=interval_image)

    output_img.save(temppath + 'image' + str(i).rjust(3, '0') + '.PNG')
    print("saved")



def animateIt(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image,
              ammountOfFrames, frameRate, randomness):

    input_img.save('input.png')

    listDir = os.listdir(temppath)
    for f in listDir:
        os.remove(temppath + f)
    procs = []
    for i in range(ammountOfFrames):
        pr = mp.Process(target=pixsort, args=(sorting_function, interval_function, angle, clength, interval_image, randomness, i) )
        #pr.daemon = True
        procs.append(pr)
        pr.start()
    for proc in procs:
        proc.join()
    for proc in procs:
        proc.terminate()
    # r? r блять? Как я до этого должен додуматься блядь
    (
        ffmpeg
        .input(temppath + "image%03d.PNG")
        .output("movie.mp4", r=frameRate)
        .run(overwrite_output=True)
    )

    return "movie.mp4"