import time
import sys
sys.path.append("/rpi_ws281x/python")
import webcolors
from neopixel import *
# LED strip configuration:
LED_COUNT = 100      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LIGHT_MAP = {"A": 97, "B": 94, "C": 91, "D": 88, "E": 85, "F": 82, "G": 79, "H": 76, "Q": 67, "P": 65, "O": 63, "N": 60, "M": 57,
             "L": 54, "K": 51, "J": 49, "I": 46, "R": 32, "S": 29, "T": 27, "U": 25, "V": 22, "W": 20, "X": 17, "Y": 15, "Z": 13, " ": 0}
LIGHT_COLORS = ["Aqua", "Blue", "Green", "Yellow", "Red", "Orange"]
#implementation
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                          LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()


def mapLights():
    result = []
    for i in range(strip.numPixels()):
        colorIndex = i % len(LIGHT_COLORS)
        result.append(LIGHT_COLORS[colorIndex])
    return result

mappedLights = mapLights()

def formatColor(color):
    result = []
    rgbColor = webcolors.html5_parse_legacy_color(str(color))
    for i in rgbColor:
        result.append(int(i))
    return result

def setAllLightColors():
    for i in range(strip.numPixels()):
        color = formatColor(mappedLights[i])
        strip.setPixelColor(i, Color(color[0], color[1], color[2]))
    
def turnOffAll():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def turnOnAll():
    setAllLightColors()
    strip.show()
def blink():
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()
    turnOffAll()
    turnOnAll()

def mapLed(message):
    results = []
    for i in message:
        number = LIGHT_MAP.get(i)
        results.append(number)
    return (results)

def sendMessage(message):
    mappedLed = mapLed(message.upper())
    blink()
    turnOffAll()
    for i in mappedLed:
        color = formatColor(mappedLights[i])
        strip.setPixelColor(i, Color(color[0], color[1], color[2]))
        strip.show()
        time.sleep(1.5)
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
    blink()
    turnOnAll()
