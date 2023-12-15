from PIL import Image, ImageFilter, ImageChops

InputImage = Image.open('E:/РОМАН/!хрень/1_wm.png')
InputImage.load()
InputImage = InputImage.convert(mode='RGB')

Red, Green, Blue = InputImage.split()

Red = ImageChops.offset(Red,5,0)

ImgOutput = Image.merge('RGB',(Red, Green,Blue))


ImgOutput.show()