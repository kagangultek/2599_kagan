from machine import Pin, ADC, SoftI2C, PWM
import ssd1306
from time import sleep
import utime
import machine
from servo import Servo

led_red = Pin(14, Pin.OUT)
led_green = Pin(27, Pin.OUT)
motor=Servo(pin=12)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
KEY_UP   = const(0)
KEY_DOWN = const(1)
keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]
cols = [19,16,15,23]
rows = [2,4,5,18]
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]

def init():
    for row in range(0,4):
        for col in range(0,4):
            row_pins[row].value(0)
            
def scan(row, col):
    row_pins[row].value(1)
    key = None
 
    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].value(0)
 
    return key
 
print("starting")
 
init()
 
while True:
    oled.fill(0) 
    for row in range(4):
        for col in range(4):
            key = scan(row, col)
            if key == KEY_DOWN:
                oled.text("Key Pressed: ",10,0)
                print(keys[row][col])
                oled.text(keys[row][col], 55, 30)
                oled.show()
                last_key_press = keys[row][col]
