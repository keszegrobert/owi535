#import the USB and Time librarys into Python
import usb.core, usb.util, time
from mpu6050 import mpu6050
import time
from evdev import InputDevice, ecodes
import json
from owi535 import Owi535

'''sensor = mpu6050(0x68)'''
gamepad = InputDevice('/dev/input/event4')
arm = Owi535()

try:
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_ABS:
            print event.code, event.value
            if event.code == 16:
                arm.RotateBase(event.value)
            elif event.code == 17:
                arm.RotateShoulder(event.value)
            elif event.code == 1:
                arm.RotateElbow(event.value)
            elif event.code == 4:
                arm.RotateWrist(event.value)
            else:
                pass
                # print('Unknown event code for abs:', event.code, event.value)
        elif event.type == ecodes.EV_KEY:
            if event.code == 308:
                arm.SwitchLight(event.value)
            elif event.code == 305:
                arm.OpenGrip(event.value)
            elif event.code == 307:
                arm.CloseGrip(event.value)
            else:
                pass
                # print("Unknown event code:", event.code)
        else:
            pass
            # print("Unknown event type: ", event.type)
        arm.StartMove()


except Exception as e:
    arm.StopMove()
    print(e)
