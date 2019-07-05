import board
import time
import neopixel



#one lightning flash
def plumeLight(strip, firstpixel):
    for a in range(44):
        strip[a+firstpixel]=(255, 255, 255)
    strip.show()
    for a in range(44):
        strip[a+firstpixel]=(0, 0, 0)
    strip.show()
    for a in range(44):
        strip[a+firstpixel]=(255, 255, 255)
    strip.show()
    for a in range(44):
        strip[a+firstpixel]=(0, 0, 0)
    strip.show()

#workaround around the maximum value

def plumeLight2(strip, firstpixel):
    for a in range(44):
        strip[a+firstpixel+307]=(255, 255, 255)
    strip.show()
    for a in range(44):
        strip[a+firstpixel+307]=(0, 0, 0)
    strip.show()
    for a in range(44):
        strip[a+firstpixel+307]=(255, 255, 255)
    strip.show()
    for a in range(44):
        strip[a+firstpixel+307]=(0, 0, 0)
    strip.show()