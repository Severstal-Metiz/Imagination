from pixelsort import pixelsort
import ffmpeg
import os
import time
from PIL import Image
import PIL

import multiprocessing as mp

temppath = 'temp/'


def InitTempDir():
    os.makedirs(temppath, exist_ok=True)
    listDir = os.listdir(temppath)
    for f in listDir:
        os.remove(temppath + f)

def pixsort(sorting_function, interval_function, angle, clength, interval_image, randomness, i):
    t_s = time.perf_counter()
    img = Image.open('input.png')
    print(f"{i}img opened")
    output_img = pixelsort(img, sorting_function=sorting_function,
                           interval_function=interval_function, randomness=randomness, angle=angle, clength=clength,
                           interval_image=interval_image)
    print(f"{i}img sorted")
    output_img.save(temppath + 'image' + str(i).rjust(3, '0') + '.PNG')
    prc_time = time.perf_counter() - t_s
    print(f"{i} img saved. Time: {prc_time}")



def animateIt(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image,
              ammountOfFrames, frameRate, randomness):

    InitTempDir()
    input_img.save('input.png')
    procs = []

    for i in range(ammountOfFrames):
        pr = mp.Process(target=pixsort, args=(sorting_function, interval_function, angle, clength, interval_image, randomness, i) )
        #pr.daemon = True
        procs.append(pr)
        pr.start()
        print(f"{i} proc started")
    for proc in procs:
        proc.join()
        print("joined")
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