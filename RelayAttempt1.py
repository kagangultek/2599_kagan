from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306

sensor = dht.DHT11(Pin(14))
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
relay1 = Pin(12, Pin.OUT)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
  try:
    sleep(1)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    tempValue = str(temp)
    humValue = str(hum)
    oled.text(tempValue, 0, 10)
    oled.text(humValue, 0, 20)
    oled.show
    oled.fill(0)
    if hum >= 60:
        relay1.value(1)
    else:
        relay1.value(0)
  except OSError as e:
    print('Failed to read sensor.')
