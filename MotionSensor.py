''' Note : This code cannot work using the Android application as the sensor needs a VOUT port to be used
To make both the motion sensor and the Android Application work together use a level shifter and soilder
the ultrasonic sensor to the 3.3V port'''
import Ambience
import board
from hcsr04 import HCSR04
trig = board.A4
echo = board.A5

with HCSR04(trig, echo) as sonar:
    try:
        while True:
            distance = sonar.dist_cm
            if(distance <= 20):
                '# top flash'''
                for j in range(616)
                    strip[j]=(0, 0, 255)
                strip.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                strip.show()
                for j in range(616)
                    strip[j]=(0, 0, 255)
                strip.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                strip.show()
                '# top and bottom flash'''
                 for j in range(616)
                    strip[j]=(0, 0, 255)
                    strip3[j]=(0, 0, 255)
                strip.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                    strip3[j]=(0, 0, 0)
                strip.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 255)
                    strip3[j]=(0, 0, 255)
                strip.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                    strip3[j]=(0, 0, 0)
                strip.show()
                strip3.show()
                'everything flashes'''
                 for j in range(616)
                    strip[j]=(0, 0, 255)
                    strip2[j]=(0, 0, 255)
                    strip3[j]=(0, 0, 255)
                strip.show()
                strip2.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                    strip2[j]=(0, 0, 0)
                    strip3[j]=(0, 0, 0)
                strip.show()
                strip2.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 255)
                    strip2[j]=(0, 0, 255)
                    strip3[j]=(0, 0, 255)
                strip.show()
                strip2.show()
                strip3.show()
                for j in range(616)
                    strip[j]=(0, 0, 0)
                    strip2[j]=(0, 0, 0)
                    strip3[j]=(0, 0, 0)
                strip.show()
                strip2.show()
                strip3.show()
            if (distance >20 and distance <50):
                Ambience.AmbienceDark()
            if (distance>50 and distance != 716):
                Ambience.AmbienceLight()


    except KeyboardInterrupt:
        pass