from threading import Timer
import schedule
import time
from board import SCL,SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor


def wipe_me():
    print('..initializing')
    
    #I2C bus interface
    i2c_bus=(busio.I2C(SCL, SDA))

    #Class instance
    pca=PCA9685(i2c_bus)

    #PWM frquency = 50 Hz
    pca.frequency = 50

    #For SER-110X, PWM range is 850μs - 2350 μs)
    servoBR = servo.Servo(pca.channels[0], min_pulse=850, max_pulse=2350)

    # Repeats the loop 3 times, then exits.
    num = 3
    for x in range(num):
            for i in range(180):
                servoBR.angle = i
                time.sleep(0.005)
                print("Swish")
            for i in range(180):
                servoBR.angle = 180 - i
                time.sleep(0.005)
                print("Swoosh")
    pca.deinit()
    print("Done! I can finally see again!")

# For every n minutes: schedule.every(n).minutes.do(wipe_me)
# For every n hour: schedule.every(n).hour.do(wipe_me)
# Every day at 12 or 00: schedule.every().day.at("00:00").do(wipe_me)
schedule.every(5).seconds.do(wipe_me)
while True:
    schedule.run_pending()
    time.sleep(1)
