# RasPiThrottleControl v(1.0.0)
# Author: Timothy Cochran v(1.0.0)
#
# Purpose: The purpose of this program is to provide a signal that can drive an EDC for
# Brushless DC motors (BLDC) using Pulse Width Modulation (PWM). The EDC requires a 50hz
# wave with a pulse of 1-2ms (5-10% Duty Cycle) where 1ms is 0% throttle and 2ms is 100%
# throttle. This program will convert a throttle percent to the required duty cycle
# that the RPi.GPIO library uses. 
#
# Package Instillation Notes: If debugging on a machine that is NOT a raspberry pi, you
# will recieve an error. This library can only be run on a raspberry pi. You can install 
# the package by using 'pip3 install RPi.GPIO' in the terminal on your rasPi. RPi.GPIO
# information can be found at https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/ 
# -------------------------------------------------------------------------------------------

import RPi.GPIO as GPIO

freq = 50                       #global PMW frequency (50Hz standard for Servo/Motor Control)
PMWPin = 12                     #global GPIO pin to output onto

GPIO.setmode(GPIO.BOARD)        #Sets GPIO pins to standard pin-out
GPIO.setup(PMWPin, GPIO.OUT)    #Pin initialization 

uExit = False                   #uExit initialization
p = GPIO.PWM(PMWPin, freq)      #pin initialization for PWM


while (uExit == False):
    #Try block for checking user input and exiting when a number is not input
    #throtPercent is converting a user input percent to a duty cycle ranging from
    #5% to 10% 
    try:
        throtPercent = (.05 * (float(input("Throttle Percent(0-100): ")))) + 5
    except ValueError:
        uExit = True

    #Input range check
    if (uExit == False):
        if(throtPercent < 5 or throtPercent > 10):
            print("--------INVALID ENTRY--------\nValue must be between 0 and 100")
        else:
            p.start(throtPercent)
    

print("Goodbye!")
p.stop()                        #stops PWM on your pin
GPIO.cleanup()                  #cleans-up any code running on the pins

