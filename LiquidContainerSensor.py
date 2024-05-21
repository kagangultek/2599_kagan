from machine import Pin, ADC, SoftI2C, PWM
from time import sleep
import ssd1306
from servo import Servo


SensorValue = ADC(Pin(4))
Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)
led_red = Pin(23, Pin.OUT)
led_green = Pin(18, Pin.OUT)
led_yellow = Pin(5, Pin.OUT)
motor=Servo(pin=19)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    oled.fill(0)
    PotValue = Pot.read()
    PotValueText = str(PotValue)
    oled.text("Pot degeri", 0, 20)
    oled.text(PotValueText, 0, 30)
    led_yellow.value(1)
    led_green.value(0)
    led_red.value(0)
    oled.show()
    sleep(1)  
    while PotValue <= 2000:
        led_yellow.value(0)
        PotValue = Pot.read()
        PotValueText = str(PotValue)
        oled.text("Pot degeri", 0, 20)
        oled.text(PotValueText, 0, 30)
        SensorRead = SensorValue.read()
        print(SensorRead)
        oled.show()
        if SensorRead >= 500:
            led_red.value(0)
            led_green.value(1)
            oled.text('Su Tahliye Ediliyor', 0, 0)
            oled.show()
            oled.fill(0)
            motor.move(90)
        elif SensorRead < 500:
            led_red.value(1)
            led_green.value(0)
            oled.text('Su Yeterli Degil', 0, 0)
            oled.show()
            oled.fill(0)
            motor.move(0)
        sleep(0.7)
        
