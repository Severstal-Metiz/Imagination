from pixelsort import pixelsort
from PIL import Image
import ffmpeg
import os
temppath = 'temp/'

def animateIt(input_img,mask_image,sorting_function,interval_function, angle,clength,interval_image, ammountOfFrames, frameRate,randomness):
    listDir = os.listdir(temppath)
    for f in listDir:
        os.remove(temppath + f)
    frames = [0]*ammountOfFrames
    #angle = 0
    for i in range(ammountOfFrames):
        new_frame = pixelsort(input_img,mask_image, sorting_function=sorting_function, interval_function=interval_function, randomness=randomness,angle=angle,clength=clength, interval_image=interval_image)
        frames[i] = new_frame
        #randomness -= 10
        #angle +=30
        new_frame.save(temppath + 'image'+ str(i).rjust(3,'0') + '.PNG')
    
    # Save into a GIF file that loops forever
    (
        ffmpeg
        .input(temppath + "image%03d.PNG", frameRate)
        .output("movie.mp4")
        .run(overwrite_output=True)
    )
    #frames[0].save('pixsort.gif', format='GIF', append_images=frames[1:], save_all=True, duration=frameDuration, loop=0)
    return new_frame #'pixsort.gif'

def pixsort(input_img,mask_image,sorting_function,interval_function, randomness,angle,clength,interval_image):
    output_img = pixelsort(input_img,mask_image, sorting_function=sorting_function, interval_function=interval_function, randomness=randomness,angle=angle,clength=clength,interval_image=interval_image)
    return output_img