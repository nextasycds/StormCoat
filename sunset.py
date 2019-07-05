
import asyncio_slow as asyncio

@asyncio.coroutine
#function that gradually changes each pixel of the strip based on the starting and ending color of the strip
def gradientWipe(strip, red1, green1, blue1, red2, green2, blue2):

a=43
b=87
c=131
d=175
e=219
f=263
g=307
h=351
i=395
j=439
k=483
k=527
l=571
m=615

# --------------------CASE 1 only red changes ----------------------

    if(red1!=red2 and green1=green2 and blue1=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (red2-red1), 2):
                strip[z]=(red1+x, green1, blue1)
                strip[a]=(red1+x, green1, blue1)
                strip[b]=(red1+x, green1, blue1)
                strip[c]=(red1+x, green1, blue1)
                strip[d]=(red1+x, green1, blue1)
                strip[e]=(red1+x, green1, blue1)
                strip[f]=(red1+x, green1, blue1)
                strip[g]=(red1+x, green1, blue1)
                strip[h]=(red1+x, green1, blue1)
                strip[i]=(red1+x, green1, blue1)
                strip[j]=(red1+x, green1, blue1)
                strip[k]=(red1+x, green1, blue1)
                strip[l]=(red1+x, green1, blue1)
                strip[m]=(red1+x, green1, blue1)
            strip.show()


# --------------------CASE 2 only green changes ----------------------

    if(red1=red2 and green1!=green2 and blue1=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (green1-green2), 2):
                strip[z]=(red1, green1-x, blue1)
                strip[a]=(red1, green1-x, blue1)
                strip[b]=(red1, green1-x, blue1)
                strip[c]=(red1, green1-x, blue1)
                strip[d]=(red1, green1-x, blue1)
                strip[e]=(red1, green1-x, blue1)
                strip[f]=(red1, green1-x, blue1)
                strip[g]=(red1, green1-x, blue1)
                strip[h]=(red1, green1-x, blue1)
                strip[i]=(red1, green1-x, blue1)
                strip[j]=(red1, green1-x, blue1)
                strip[k]=(red1, green1-x, blue1)
                strip[l]=(red1, green1-x, blue1)
                strip[m]=(red1, green1-x, blue1)
            strip.show()
# --------------------CASE 3 only blue changes ----------------------

    if(red1=red2 and green1=green2 and blue1!=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (blue2-blue1), 2):
                strip[z]=(red1, green1, blue1+x)
                strip[a]=(red1, green1, blue1+x)
                strip[b]=(red1, green1, blue1+x)
                strip[c]=(red1, green1, blue1+x)
                strip[d]=(red1, green1, blue1+x)
                strip[e]=(red1, green1, blue1+x)
                strip[f]=(red1, green1, blue1+x)
                strip[g]=(red1, green1, blue1+x)
                strip[h]=(red1, green1, blue1+x)
                strip[i]=(red1, green1, blue1+x)
                strip[j]=(red1, green1, blue1+x)
                strip[k]=(red1, green1, blue1+x)
                strip[l]=(red1, green1, blue1+x)
                strip[m]=(red1, green1, blue1+x)
            strip.show()
# --------------------CASE 4 red and green change ----------------------
if(red1!=red2 and green1!=green2 and blue1=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (red2-red1), 2):
                strip[z]=(red1+x, green1, blue1)
                strip[a]=(red1+x, green1, blue1)
                strip[b]=(red1+x, green1, blue1)
                strip[c]=(red1+x, green1, blue1)
                strip[d]=(red1+x, green1, blue1)
                strip[e]=(red1+x, green1, blue1)
                strip[f]=(red1+x, green1, blue1)
                strip[g]=(red1+x, green1, blue1)
                strip[h]=(red1+x, green1, blue1)
                strip[i]=(red1+x, green1, blue1)
                strip[j]=(red1+x, green1, blue1)
                strip[k]=(red1+x, green1, blue1)
                strip[l]=(red1+x, green1, blue1)
                strip[m]=(red1+x, green1, blue1)
            strip.show()
            for x in range(0, (green2-green1), 2):
                strip[z]=(red2, green1+x, blue1)
                strip[a]=(red2, green1+x, blue1)
                strip[b]=(red2, green1+x, blue1)
                strip[c]=(red2, green1+x, blue1)
                strip[d]=(red2, green1+x, blue1)
                strip[e]=(red2, green1+x, blue1)
                strip[f]=(red2, green1+x, blue1)
                strip[g]=(red2, green1+X, blue1)
                strip[h]=(red2, green1+X, blue1)
                strip[i]=(red2, green1+x, blue1)
                strip[j]=(red2, green1+x, blue1)
                strip[k]=(red2, green1+x, blue1)
                strip[l]=(red2, green1+x, blue1)
                strip[m]=(red2, green1, blue1)
            strip.show()

# --------------------CASE 5 green and blue change -------------------
if(red1=red2 and green1!=green2 and blue1!=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (blue2-blue1), 2):
                strip[z]=(red1, green1, blue1+x)
                strip[a]=(red1, green1, blue1+x)
                strip[b]=(red1, green1, blue1+x)
                strip[c]=(red1, green1, blue1+x)
                strip[d]=(red1, green1, blue1+x)
                strip[e]=(red1, green1, blue1+x)
                strip[f]=(red1, green1, blue1+x)
                strip[g]=(red1, green1, blue1+x)
                strip[h]=(red1, green1, blue1+x)
                strip[i]=(red1, green1, blue1+x)
                strip[j]=(red1, green1, blue1+x)
                strip[k]=(red1, green1, blue1+x)
                strip[l]=(red1, green1, blue1+x)
                strip[m]=(red1, green1, blue1+x)
            strip.show()
            for x in range(0, (green2-green1), 2):
                strip[z]=(red1, green1+x, blue2)
                strip[a]=(red1, green1+x, blue2)
                strip[b]=(red1, green1+x, blue2)
                strip[c]=(red1, green1+x, blue2)
                strip[d]=(red1, green1+x, blue2)
                strip[e]=(red1, green1+x, blue2)
                strip[f]=(red1, green1+x, blue2)
                strip[g]=(red1, green1+X, blue2)
                strip[h]=(red1, green1+X, blue2)
                strip[i]=(red1, green1+x, blue2)
                strip[j]=(red1, green1+x, blue2)
                strip[k]=(red1, green1+x, blue2)
                strip[l]=(red1, green1+x, blue2)
                strip[m]=(red1, green1, blue1)
            strip.show()
# --------------------CASE 6 red and blue change -------------------
if(red1!=red2 and green1=green2 and blue1!=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (blue2-blue1), 2):
                strip[z]=(red1, green1, blue1+x)
                strip[a]=(red1, green1, blue1+x)
                strip[b]=(red1, green1, blue1+x)
                strip[c]=(red1, green1, blue1+x)
                strip[d]=(red1, green1, blue1+x)
                strip[e]=(red1, green1, blue1+x)
                strip[f]=(red1, green1, blue1+x)
                strip[g]=(red1, green1, blue1+x)
                strip[h]=(red1, green1, blue1+x)
                strip[i]=(red1, green1, blue1+x)
                strip[j]=(red1, green1, blue1+x)
                strip[k]=(red1, green1, blue1+x)
                strip[l]=(red1, green1, blue1+x)
                strip[m]=(red1, green1, blue1+x)
            strip.show()
            for x in range(0, (red2-red1), 2):
                strip[z]=(red1+x, green1, blue2)
                strip[a]=(red1+x, green1, blue2)
                strip[b]=(red1+x, green1, blue2)
                strip[c]=(red1+x, green1, blue2)
                strip[d]=(red1+x, green1, blue2)
                strip[e]=(red1+x, green1, blue2)
                strip[f]=(red1+x, green1, blue2)
                strip[g]=(red1+x, green1, blue2)
                strip[h]=(red1+x, green1, blue2)
                strip[i]=(red1+x, green1, blue2)
                strip[j]=(red1+x, green1, blue2)
                strip[k]=(red1+x, green1, blue2)
                strip[l]=(red1+x, green1, blue2)
                strip[m]=(red1+x, green1, blue2)
            strip.show()
# --------------------CASE 7 EVERYRTHING CHANGES -------------------
if(red1!=red2 and green1!=green2 and blue1!=blue2)

        for z in range(0, 44, 2):
        a++
        b++
        c++
        d++
        e++
        f++
        g++
        h++
        i++
        j++
        k++
        l++
        m++
            for x in range(0, (blue2-blue1), 2):
                strip[z]=(red1, green1, blue1+x)
                strip[a]=(red1, green1, blue1+x)
                strip[b]=(red1, green1, blue1+x)
                strip[c]=(red1, green1, blue1+x)
                strip[d]=(red1, green1, blue1+x)
                strip[e]=(red1, green1, blue1+x)
                strip[f]=(red1, green1, blue1+x)
                strip[g]=(red1, green1, blue1+x)
                strip[h]=(red1, green1, blue1+x)
                strip[i]=(red1, green1, blue1+x)
                strip[j]=(red1, green1, blue1+x)
                strip[k]=(red1, green1, blue1+x)
                strip[l]=(red1, green1, blue1+x)
                strip[m]=(red1, green1, blue1+x)
            strip.show()
            for x in range(0, (red2-red1), 2):
                strip[z]=(red1+x, green1, blue2)
                strip[a]=(red1+x, green1, blue2)
                strip[b]=(red1+x, green1, blue2)
                strip[c]=(red1+x, green1, blue2)
                strip[d]=(red1+x, green1, blue2)
                strip[e]=(red1+x, green1, blue2)
                strip[f]=(red1+x, green1, blue2)
                strip[g]=(red1+x, green1, blue2)
                strip[h]=(red1+x, green1, blue2)
                strip[i]=(red1+x, green1, blue2)
                strip[j]=(red1+x, green1, blue2)
                strip[k]=(red1+x, green1, blue2)
                strip[l]=(red1+x, green1, blue2)
                strip[m]=(red1+x, green1, blue2)
            strip.show()
             for x in range(0, (green2-green1), 2):
                strip[z]=(red2, green1+x, blue2)
                strip[a]=(red2, green1+x, blue2)
                strip[b]=(red2, green1+x, blue2)
                strip[c]=(red2, green1+x, blue2)
                strip[d]=(red2, green1+x, blue2)
                strip[e]=(red2, green1+x, blue2)
                strip[f]=(red2, green1+x, blue2)
                strip[g]=(red2, green1+x, blue2)
                strip[h]=(red2, green1+x, blue2)
                strip[i]=(red2, green1+x, blue2)
                strip[j]=(red2, green1+x, blue2)
                strip[k]=(red2, green1+x, blue2)
                strip[l]=(red2, green1+x, blue2)
                strip[m]=(red2, green1+X, blue2)
            strip.show()



tasks = [
    asyncio.Task(gradientWipe(strip, 255, 170, 0, 255, 106, 89),
    asyncio.Task(gradientWipe(strip2, 255, 210, 0, 255, 170, 0),
 ]

 tasks2 = [
    asyncio.Task(gradientWipe(strip, 255, 106, 89, 200, 0, 255),
    asyncio.Task(gradientWipe(strip2, 255, 170, 0, 255, 106, 89),
    asyncio.Task(gradientWipe(strip3, 255, 210, 0, 255, 170, 0)
]

tasks3 = [
    asyncio.Task(gradientWipe(strip2, 255, 106, 89, 200, 0, 255),
    asyncio.Task(gradientWipe(strip3, 255, 170, 0, 255, 106, 89)
]



def sunset(strip, strip2, strip3):
    for j in range(0, 616, 2):  #light one pixel out of two
        strip[j]=(255, 210, 0)
        strip2[j]=(255, 210, 0)
        strip3[j]=(255, 210, 0)
    strip.show()
#applying gradient Wipe to each

gradientWipe(strip, 255, 210, 0, 255, 170, 0)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.wait(tasks2))
loop.run_until_complete(asyncio.wait(tasks3))
loop.close()
gradientWipe(strip3, 255, 106, 89, 200, 0, 255)
