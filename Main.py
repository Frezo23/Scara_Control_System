from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import board

import time
import tkinter as tk
from tkinter import *
import math
import random


kit = MotorKit(i2c=board.I2C())
kit2 = MotorKit(i2c=board.I2C(),address=0x61)

delay = 0.00001

switch_1 = False
switch_2 = False
switch_3 = False

step_1 = kit.stepper1()   ### First Arm
step_2 = kit.stepper2()   ### Second Arm
step_3 = kit2.stepper1()  ### Z Axis

pos_1 = 0
pos_2 = 0
pos_3 = 0

    
def Motor_1(direction): ### This motor, has a belt reduction of [1 To 5] 20-100
    global delay, pos_1
    
    if direction == 'b'or'B':
        step_1.onestep(direction=stepper.BACKWARD)
        time.sleep(delay)
    elif direction == 'f'or'F':
        step_1.onestep()
        time.sleep(delay)
    else:
        print('Wrong Direction Argument for [First Motor]!!!')
        pass

def Motor_2(direction): ### This motor, has a belt reduction of [1 To 3] 20-60
    global delay, pos_2
    
    if direction == 'b'or'B':
        step_2.onestep(direction=stepper.BACKWARD)
        time.sleep(delay)
    elif direction == 'f'or'F':
        step_2.onestep()
        time.sleep(delay)
    else:
        print('Wrong Direction Argument for [Second Motor]!!!')
        pass
    
def Z_Axis(direction):
    global delay, pos_3
    
    if direction == 'b'or'B':
        step_3.onestep(direction=stepper.BACKWARD)
        time.sleep(delay)
    elif direction == 'f'or'F':
        step_3.onestep()
        time.sleep(delay)
    else:
        print('Wrong Direction Argument for [Z Axis Motor]!!!')
        pass
    
def Homing_Sequence():
    global delay, pos_1, pos_2, pos_3, switch_1, switch_2, switch_3
    
    arm_1_home = False
    arm_2_home = False
    arm_3_home = False
    
    while arm_1_home == False:
        Motor_1('f')
        
        if switch_1 == True:
            arm_1_home = True
    
    while arm_2_home == False:
        Motor_2('f')
        
        if switch_2 == True:
            arm_2_home = True
        
    while arm_3_home == False:
        Z_Axis('f')
        
        if switch_3 == True:
            arm_3_home = True
        
    