from threading import Timer
import time
from board import SCL,SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor

print('..initializing')

#I2C bus interface
i2c_bus=(busio.I2C(SCL, SDA))
#Class instance
pca=PCA9685(i2c_bus)
#PWM frquency = 50 Hz
pca.frequency = 50

#For SER-110X, PWM range is 850μs - 2350 μs)
servoBR = servo.Servo(pca.channels[0], min_pulse=850, max_pulse=2350)

while True:
    user_control = input('Press 1 to start wiping and 2 to stop')
    if user_control == '1':
        for i in range(148):
            servoBR.angle = i
            time.sleep(0.005)
            print("Swish")
        for i in range(148):
            servoBR.angle = 148 - i
            time.sleep(0.005)
            print("Swoosh")
    elif user_control == '2':
        pca.deinit()
        print("Done! I can finally see again!")
        break

