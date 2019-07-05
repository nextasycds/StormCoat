'#Nextasy x MarkAntoine collaboration - June 2019'

import time
import board
import busio
import lightning
import spiral
import neopixel
import Ambience
from adafruit_circuitplayground.express import cpx

#initializing the strips
pixpin = board.A1
pixpin2 = board.A2
pixpin3 = board.A3
numpix = 340


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.5, auto_write=False)
strip2 = neopixel.NeoPixel(pixpin2, numpix, brightness=0.5, auto_write=False)
strip3 = neopixel.NeoPixel(pixpin3, numpix, brightness=0.5, auto_write=False)

#initializing bluetotooth serial communication

uart = busio.UART(board.TX, board.RX, baudrate=9600)

#turn off the whole coat



def plumeLightOFFALL():
    for j in range(len(strip)):
        strip[j]=(0, 0, 0)
        strip2[j]=(0, 0, 0)
        strip3[j]=(0, 0, 0)
    strip.show()
    strip2.show()
    strip3.show()

#color bank

RED = (255, 0, 0)

while True:
    data = uart.readline()  # read a line
    #print(data)
    #if data is None:  # Data was not received
        #plumeLightOFFALL()
#turning feathers on individually, multiple input options in case the button is clicked more than once
    if data == b'1':
        lightning.plumeLight(strip, 0)
    if data == b'2':
        lightning.plumeLight(strip, 43)
    if data == b'3':
        lightning.plumeLight(strip, 87)
    if data == b'4':
        lightning.plumeLight(strip, 131)
    if data == b'5':
        lightning.plumeLight(strip, 175)
    if data == b'6':
        lightning.plumeLight(strip, 219)
    if data == b'7':
        lightning.plumeLight(strip, 263)
    if data == b'8':
        lightning.plumeLight(strip, 307)
    if data == b'9':
        lightning.plumeLight(strip, 44)
    if data == b'a':
        lightning.plumeLight(strip, 395)
    if data == b'b':
        lightning.plumeLight(strip, 439)
    if data == b'c':
        lightning.plumeLight(strip, 483)
    if data == b'd':
        lightning.plumeLight(strip, 527)
    if data == b'e':
        lightning.plumeLight(strip, 550)
    if data == b'f':
        lightning.plumeLight(strip, 615)
    if data == b'g':
        lightning.plumeLight(strip2, 0)
    if data == b'h':
        lightning.plumeLight(strip2, 43)
    if data == b'i':
        lightning.plumeLight(strip2, 87)
    if data == b'j':
        lightning.plumeLight(strip2, 131)
    if data == b'k':
        lightning.plumeLight(strip2, 175)
    if data == b'l':
        lightning.plumeLight(strip2, 219)
    if data == b'm':
        lightning.plumeLight(strip2, 263)
    if data == b'n':
        lightning.plumeLight(strip2, 307)
    if data == b'o':
        lightning.plumeLight(strip2, 44)
    if data == b'p':
        lightning.plumeLight(strip2, 395)
    if data == b'q':
        lightning.plumeLight(strip2, 439)
    if data == b'r':
        lightning.plumeLight(strip2, 483)
    if data == b's':
        lightning.plumeLight(strip2, 527)
    if data == b't':
        lightning.plumeLight(strip2, 550)
    if data == b'u':
        lightning.plumeLight(strip2, 615)
    if data == b'v':
        lightning.plumeLight(strip3, 0)
    if data == b'w':
        lightning.plumeLight(strip3, 43)
    if data == b'x':
        lightning.plumeLight(strip3, 87)
    if data == b'y':
        lightning.plumeLight(strip3, 131)
    if data == b'z':
        lightning.plumeLight(strip3, 175)
    if data == b'A':
        lightning.plumeLight(strip3, 219)
    if data == b'B':
        lightning.plumeLight(strip3, 263)
    if data == b'C':
        lightning.plumeLight(strip3, 307)
    if data == b'D':
        lightning.plumeLight(strip3, 44)
    if data == b'E':
        lightning.plumeLight(strip3, 395)
    if data == b'F':
        lightning.plumeLight(strip3, 439)
    if data == b'G':
        lightning.plumeLight(strip3, 483)
    if data == b'H':
        lightning.plumeLight(strip3, 527)
    if data == b'I':
        lightning.plumeLight(strip3, 550)
    if data == b'J':
        lightning.plumeLight(strip3, 615)
    if data == b'N':
        sunset.sunset()
    if data == b'O':
        spiral.colorWipe((172, 172, 172), 0, strip)
        spiral.colorWipe((172, 172, 172), 0, strip2)
        spiral.colorWipe(((172, 172, 172), 0, strip3)
    if data == b'P':
        Ambience.Ambience()