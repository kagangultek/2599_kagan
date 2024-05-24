from machine import Pin, SoftI2C, ADC, PWM
import time
import ssd1306

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
Red = Pin(15, Pin.OUT)
Red = Pin(15, Pin.OUT)
Blue = Pin(2, Pin.OUT)
Green = Pin(4, Pin.OUT)
Buzzer = Pin(13, Pin.OUT)
ir_sensor = Pin(23, Pin.IN)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
KEY_UP   = const(0)
KEY_DOWN = const(1)
keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]
cols = [27,14,12,35]
rows = [26,25,33,32]
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

init()

while True:
    for row in range(4):
        for col in range(4):
            key = scan(row, col)
            if key == KEY_DOWN:
                print(keys[row][col])
                last_key_press = keys[row][col]
                
while last_key_press == A:
    time.sleep(0.5)
    pot_value = pot.read()
    print(pot_value)
    sensor_state = ir_sensor.value()
    oled.fill(0)
    oled.text("sistem kapali", 0, 20)
    oled.show()
    Red.value(0)
    Blue.value(0)
    Buzzer.value(0)
    Green.value(0)
    print(sensor_state)
    if pot_value >= 1500:
        oled.fill(0)
        oled.show
        if sensor_state == 0:
            Green.value(1)
            oled.text("kapi kapali", 0, 10)
            oled.show()
        if sensor_state == 1:
            Red.value(1)
            oled.text("kapi acik", 0, 10)
            Buzzer.value(1)
            oled.show()




