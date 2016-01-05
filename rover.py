import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

channel_1_dir = "P9_11"
channel_2_dir = "P9_12"
channel_3_dir = "P9_13"
channel_4_dir = "P9_15"
channel_1_pwm = "P9_14"
channel_2_pwm = "P8_13"
channel_3_pwm = "P9_42"
channel_4_pwm = "P9_21"

def init_rover():
	GPIO.setup(channel_1_dir, GPIO.OUT)
	GPIO.setup(channel_2_dir, GPIO.OUT)
	GPIO.setup(channel_3_dir, GPIO.OUT)
	GPIO.setup(channel_4_dir, GPIO.OUT)
	GPIO.output(channel_1_dir, GPIO.HIGH)
	GPIO.output(channel_2_dir, GPIO.HIGH)
	GPIO.output(channel_3_dir, GPIO.LOW)
	GPIO.output(channel_4_dir, GPIO.LOW)
	PWM.start(channel_1_pwm, 0.0)
	PWM.start(channel_2_pwm, 0.0)
	PWM.start(channel_3_pwm, 0.0)
	PWM.start(channel_4_pwm, 0.0)
	time.sleep(0.2)
	PWM.set_frequency(channel_1_pwm, 250)
	PWM.set_frequency(channel_2_pwm, 250)
	PWM.set_frequency(channel_3_pwm, 250)
	PWM.set_frequency(channel_4_pwm, 250)


def forward(duty):
	GPIO.output(channel_1_dir, GPIO.HIGH)
	GPIO.output(channel_2_dir, GPIO.HIGH)
	GPIO.output(channel_3_dir, GPIO.LOW)
	GPIO.output(channel_4_dir, GPIO.LOW)
	PWM.set_duty_cycle(channel_1_pwm, duty)
	PWM.set_duty_cycle(channel_2_pwm, duty)
	PWM.set_duty_cycle(channel_3_pwm, duty)
	PWM.set_duty_cycle(channel_4_pwm, duty)

def backward(duty):
	GPIO.output(channel_1_dir, GPIO.LOW)
	GPIO.output(channel_2_dir, GPIO.LOW)
	GPIO.output(channel_3_dir, GPIO.HIGH)
	GPIO.output(channel_4_dir, GPIO.HIGH)
	PWM.set_duty_cycle(channel_1_pwm, duty)
	PWM.set_duty_cycle(channel_2_pwm, duty)
	PWM.set_duty_cycle(channel_3_pwm, duty)
	PWM.set_duty_cycle(channel_4_pwm, duty)

def stop():
	PWM.set_duty_cycle(channel_1_pwm, 0)
	PWM.set_duty_cycle(channel_2_pwm, 0)
	PWM.set_duty_cycle(channel_3_pwm, 0)
	PWM.set_duty_cycle(channel_4_pwm, 0)

def rotate_rover(duty, direction):
	if direction is "L":
		stop()
		GPIO.output(channel_1_dir, GPIO.LOW)
		GPIO.output(channel_2_dir, GPIO.HIGH)
		GPIO.output(channel_3_dir, GPIO.HIGH)
		GPIO.output(channel_4_dir, GPIO.LOW)
		PWM.set_duty_cycle(channel_1_pwm, duty)
		PWM.set_duty_cycle(channel_2_pwm, duty)
		PWM.set_duty_cycle(channel_3_pwm, duty)
		PWM.set_duty_cycle(channel_4_pwm, duty)
	elif direction is "R":
		GPIO.output(channel_1_dir, GPIO.HIGH)
		GPIO.output(channel_2_dir, GPIO.LOW)
		GPIO.output(channel_3_dir, GPIO.LOW)
		GPIO.output(channel_4_dir, GPIO.HIGH)
		PWM.set_duty_cycle(channel_1_pwm, duty)
		PWM.set_duty_cycle(channel_2_pwm, duty)
		PWM.set_duty_cycle(channel_3_pwm, duty)
		PWM.set_duty_cycle(channel_4_pwm, duty)
	else:
		stop()

#Test program to use all of the rover control functions. Uncomment to verify connections

init_rover()
time.sleep(1)
forward(50)
time.sleep(1)
backward(50)
time.sleep(1)
rotate_rover(50, "L")
time.sleep(1)
rotate_rover(50, "R")
time.sleep(1)
stop()
GPIO.cleanup()
PWM.cleanup()
