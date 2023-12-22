import os
temppath = 'temp/'
listDir = os.listdir(temppath)
for f in listDir:
    os.remove(temppath + f)
    #print(temppath + f)

# import ffmpeg

# for i in range(1,50):
#     print( 'image'+ str(i).rjust(3,'0') + '.PNG')



# #ffmpeg.input("/temp/*.PNG", pattern_type='glob',framerate=12).output("movie.mp4").run()

# f = ffmpeg.input("/temp/*.PNG", pattern_type='glob',framerate=12)
# f = f.output("movie.mp4")
# f.run()
