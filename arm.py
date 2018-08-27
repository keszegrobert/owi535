#import the USB and Time librarys into Python
import usb.core, usb.util, time
from mpu6050 import mpu6050
import time
from evdev import InputDevice, ecodes

sensor = mpu6050(0x68)
gamepad = InputDevice('/dev/input/event4')
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0001)
if RoboArm is None:
    raise ValueError("Arm not found")
 
def StartMove(ArmCmd):
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

def StopMove():
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    print(sensor.get_gyro_data())

try:
    for event in gamepad.read_loop():
        #filters by event type
        if event.type == ecodes.EV_ABS:
            print event.code, event.value
            if event.code == 16:
                if event.value<0:
                    StartMove([0,1,0]) #Rotate base anti-clockwise
                    print("Base forward")
                elif event.value>0:
                    StartMove([0,2,0]) #Rotate base clockwise
                    print("Base backard")
                else:
                    print("Base stop")
                    StopMove()
            elif event.code == 17:
                if event.value<0:
                    StartMove([64,0,0]) #Shoulder up
                    print("Shoulder forward")
                elif event.value>0:
                    StartMove([128,0,0]) #Shoulder down
                    print("Shoulder backward")
                else:
                    print("Shoulder stop")
                    StopMove()
            elif event.code == 1:
                if event.value<-1:
                    StartMove([16,0,0]) #Elbow up
                    print("Elbow forward")
                elif event.value>-1:
                    StartMove([32,0,0]) #Elbow down
                    print("Elbow backward")
                else:
                    print("Elbow stop")
                    StopMove()

            elif event.code == 4:
                if event.value<-1:
                    StartMove([4,0,0]) #Wrist up
                    print("Wrist forward")
                elif event.value>-1:
                    StartMove([8,0,0]) #Wrist down
                    print("Wrist backward")
                else:
                    print("Wrist stop")
                    StopMove()
            else:
                print event.code, event.value
        else:
            print "Unknown event type: ", event.type
except:
    StopMove()


'''MoveArm(1,[4,0,0]) #Wrist up
MoveArm(1,[8,0,0]) # Wrist down
MoveArm(1,[2,0,0]) #Grip open
MoveArm(1,[1,0,0]) #Grip close
MoveArm(1,[0,0,1]) #Light on
MoveArm(1,[0,0,0]) #Light off'''
