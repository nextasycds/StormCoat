


# Fill the dots one after the other with a color
def colorWipe(color, wait, stripname):
    for j in range(len(stripname)):
        stripname[j] = (color)
        time.sleep(wait)

def colorWipe2(color, wait):
    for j in range(len(strip)):
        strip2[j] = (color)
        time.sleep(wait)

def colorWipe3(color, wait):
    for j in range(len(strip)):
        strip3[j] = (color)
        time.sleep(wait)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3))

    pos -= 170
    return (0, int(pos * 3), int(255 - pos * 3))

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(strip)):
            idx = int((i * 256 / len(strip)) + j)
            strip[i] = wheel(idx & 255)
        time.sleep(wait)

def rainbow(wait):
    for j in range(255):
        for i in range(len(strip)):
            idx = int(i + j)
            strip[i] = wheel(idx & 255)
        time.sleep(wait)
