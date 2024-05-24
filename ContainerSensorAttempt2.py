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


while True:
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




