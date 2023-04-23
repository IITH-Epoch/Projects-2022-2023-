import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

motor1 = 3
motor2 = 11
motor3 = 7
motor4 = 15
gpio.setup(motor1, gpio.OUT)
gpio.setup(motor2, gpio.OUT)
gpio.setup(motor3, gpio.OUT)
gpio.setup(motor4, gpio.OUT)
freq = 50
servo1 = gpio.PWM(motor1, freq)
servo2 = gpio.PWM(motor2, freq)
servo3 = gpio.PWM(motor3, freq)
servo4 = gpio.PWM(motor4, freq)
servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)

def rotate_motor(motor, angle, prev, step):
    # Set pin 11 as an output, and define as servo1 as PWM pin
    # motor = GPIO.PWM(pin,50) # pin 11 for servo1, pulse 50Hz

    # Start PWM running, with value of 0 (pulse off)
    # motor.start(0)

    # Loop to allow user to set servo angle. Try/finally allows exit
    # with execution of servo.stop and GPIO cleanup :)
    #prev = int(input("Enter the initial angle: "))
    step = step if angle > prev else -1*step
    motor.ChangeDutyCycle(2+(prev/18))
    time.sleep(0.05)
    #angle = int(input('Enter angle between 0 & 180: '))
    for i in range(prev+step, angle, step):
        motor.ChangeDutyCycle(2+(i/18))
        time.sleep(0.1)
    #prev = angle
    time.sleep(2)
    # motor.stop()
    # motor.ChangeDutyCycle(0)
data = []
default = []
# while True:
#     motor = int(input("Enter motor number: "))
#     prev = int(input("Enter prev: "))
#     angle = int(input("Enter angle: "))
#     servo = 1
#     if (motor == 1):
#         #servo = gpio.PWM(motor1,50)
#         servo = servo1
#     elif (motor == 2):
#         #servo = gpio.PWM(motor2,50)
#         servo = servo2
#     elif (motor == 3):
#         #servo = gpio.PWM(motor3,50)
#         servo = servo3
#     else:
#         #servo = gpio.PWM(motor4,50)
#         servo = servo4
#     # if (servo == servo4):
#         # servo.start(0)
#         #rotate_motor(servo, angle, prev, 5)
#     # else:
#         # servo.start(0)
#     rotate_motor(servo, angle, prev, 5)

def move_hand(move):
    temp = str(move)
    x2 = int(temp[3])-1
    y2 = ord(temp[2])-ord('a')
    x1 = int(temp[1])-1
    y1 = ord(temp[0])-ord('a')
    ang1 = data[x1][y1]
    ang2 = data[x2][y2]
    # move from default to ang1
    rotate_motor(servo1, ang1[0], default[0], 5)
    rotate_motor(servo2, ang1[1], default[1], 5)
    rotate_motor(servo3, ang1[2], default[2], 5)
    rotate_motor(servo4, ang1[3], default[3], 5)
    # move from ang1 to ang2
    rotate_motor(servo1, ang2[0], ang1[0], 5)
    rotate_motor(servo2, ang2[1], ang1[1], 5)
    rotate_motor(servo3, ang2[2], ang1[2], 5)
    rotate_motor(servo4, ang2[3], ang1[3], 5)

#rotate_motor(servo1, 90, 0, 2)
#rotate_motor(servo2, 135, 180, 2)
#rotate_motor(servo2, 180, 135, 2)
#rotate_motor(servo3, 180, 0, 2)

def stop_servo():
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    GPIO.cleanup()
