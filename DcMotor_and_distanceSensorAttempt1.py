from machine import Pin, PWM
from dcmotor import DCMotor
from time import sleep
from hcsr04 import HCSR04
frequency = 15000

distanceSensor = HCSR04(trigger_pin="", echo_pin="", echo_timeout_us=10000)
pin1 = Pin("", Pin.OUT)
pin2 = Pin("", Pin.OUT)
enable = PWM(Pin(""), frequency)
dc_motor = DCMotor(pin1, pin2, enable)

while True:
    sleep(0.25)
    distance = distanceSensor.distance_cm()
    if distance >= 10:
        dc_motor.stop
        dc_motor.backwards(25)
    else:
        dc_motor.forward(25)
