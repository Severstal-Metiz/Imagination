from pixelsort import pixelsort
import ffmpeg
import os
import time
from PIL import Image
import multiprocessing as mp

temppath = 'temp/'

def _movie_maker():
    print()

def _init_temp_dir():
    os.makedirs(temppath, exist_ok=True)
    listDir = os.listdir(temppath)
    for f in listDir:
        os.remove(temppath + f)


def _make_movie(frame_rate):
    (
        ffmpeg
        .input(temppath + "image%03d.PNG")
        .output("movie.mp4", r=frame_rate)
        .run(overwrite_output=True)
    )

def _pixsort(sorting_function, interval_function, angle, clength, interval_image, randomness, i):

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



def make_frames_parallel(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image,
                         ammountOfFrames, frameRate, randomness):

    _init_temp_dir()
    input_img.save('input.png')

    procs = []
    for i in range(ammountOfFrames):
        pr = mp.Process(target=_pixsort, args=(sorting_function, interval_function, angle, clength, interval_image, randomness, i))
        procs.append(pr)
        pr.start()
        print(f"{i} proc started")
    for proc in procs:
        proc.join()
    for proc in procs:
        proc.terminate()

    _make_movie(frameRate)

    return "movie.mp4"

def make_frames_serial(input_img, mask_image, sorting_function, interval_function, angle, clength, interval_image,
                       ammountOfFrames, frameRate, randomness):
    _init_temp_dir()

    frames = [0] * ammountOfFrames
    for i in range(ammountOfFrames):
        new_frame = pixelsort(input_img, mask_image, sorting_function=sorting_function,
                              interval_function=interval_function, randomness=randomness, angle=angle, clength=clength,
                              interval_image=interval_image)
        frames[i] = new_frame
        new_frame.save(temppath + 'image' + str(i).rjust(3, '0') + '.PNG')

    _make_movie(frameRate)

    return "movie.mp4"
