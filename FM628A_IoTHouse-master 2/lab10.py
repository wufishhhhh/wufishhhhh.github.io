from machine import ADC, Pin
import time
import neopixel

# RGB D5
np = neopixel.NeoPixel(Pin(14), 1)

# light A0
light = ADC(0)

while True :
    bright=light.read()
    print(bright)
    if bright < 40 :
        np[0] = (10, 10, 10)
        np.write()
    else :
        np[0] = (0, 0, 0)
        np.write()
    time.sleep(.1)