#import numpy as np
from PIL import Image, ImageFilter, ImageMath, ImageOps

def KernIt(input_img, blureRadius):
    if blureRadius!=0:
        input_img = input_img.filter(ImageFilter.BoxBlur(blureRadius))	
    fgrx=(-1,0,1,-2,0,2,-1,0,1)
    fgry=(1,2,1,0,0,0,-1,-2,-1)
    ixr,ixg,ixb=input_img.filter(ImageFilter.Kernel((3,3),fgrx,1,0)).split()
    iyr,iyg,iyb=input_img.filter(ImageFilter.Kernel((3,3),fgry,1,0)).split()
    funct="convert((a+b)*5,'L')" #*5 **2
    imgr=ImageMath.eval(funct,a=ixr,b=iyr)
    imgg=ImageMath.eval(funct,a=ixg,b=iyg)
    imgb=ImageMath.eval(funct,a=ixb,b=iyb)
    output_img=Image.merge('RGB',(imgr,imgg,imgb))
    
    output_imgInv = ImageOps.invert(output_img)

    return output_img, output_imgInv