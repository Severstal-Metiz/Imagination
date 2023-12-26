from pixelsort import pixelsort
import ffmpeg
import os
import time
import multiprocessing as mp

temppath = 'temp/'


def pixsort(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image, randomness, i):
    output_img = pixelsort(input_img, mask_image, sorting_function=sorting_function,
                           interval_function=interval_function, randomness=randomness, angle=angle, clength=clength,
                           interval_image=interval_image)

    output_img.save(temppath + 'image' + str(i).rjust(3, '0') + '.PNG')

    #return 0


def animateIt(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image,
              ammountOfFrames, frameRate, randomness):
    listDir = os.listdir(temppath)
    for f in listDir:
        os.remove(temppath + f)
    procs = []
    for i in range(ammountOfFrames):
        pr = mp.Process(target=pixsort(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image, randomness, i))
        pr.daemon = True
        procs.append(pr)
        pr.start()

    for proc in procs:
        proc.terminate()
    # r? r блять? Как я до этого должен додуматься блядь
    print("HI!")
    (
        ffmpeg
        .input(temppath + "image%03d.PNG")
        .output("movie.mp4", r=frameRate)
        .run(overwrite_output=True)
    )

    return "movie.mp4"



