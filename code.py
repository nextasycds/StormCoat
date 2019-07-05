#Nextasy x MarkAntoine collaboration - June 2019

import time
import board
import busio
import lightning
import spiral
import neopixel
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
    if data==b'1':
        lightning.plumeLight(strip, 0)
    if data==b'2':
        lightning.plumeLight(strip, 43)
    if data==b'3':
        lightning.plumeLight(strip, 87)
    if data==b'4':
        lightning.plumeLight(strip, 131)
    if data==b'5':
        lightning.plumeLight(strip, 175)
    if data==b'6':
        lightning.plumeLight(strip, 219)

    if data==b'7':
        lightning.plumeLight(strip, 263)
    if data==b'8':
        lightning.plumeLight(strip, 307)
    if data==b'9':
        lightning.plumeLight(strip, 44)
    if data==b'10':
        lightning.plumeLight(strip, 395)
    if data==b'11':
        lightning.plumeLight(strip, 439)
    if data==b'12':
        lightning.plumeLight(strip, 483)
    if data==b'13':
        lightning.plumeLight(strip, 527)
    if data==b'14':
        lightning.plumeLight(strip, 550)
    if data==b'15':

        lightning.plumeLight(strip, 615)

    if data==b'40':
        spiral.colorWipe(RED, 0.1, strip)'''