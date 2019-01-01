import usb.core, usb.util, time
from owi535state import Owi535State


class Owi535:

    def __init__(self):
        self.state = Owi535State()
        self.arm = usb.core.find(idVendor=0x1267, idProduct=0x0001)
        if self.arm is None:
            raise ValueError("Arm not found")
        

    def StartMove(self):
        ArmCmd = self.state.render()
        self.arm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

    def StopMove(self):
        ArmCmd=[0,0,0]
        self.arm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
        

    def RotateBase(self, value):
        if value<0:
            self.state.startACW('base')
        elif value>0:
            self.state.startCW('base')
        else:
            self.state.stopCW('base')
            self.state.stopACW('base')

    def RotateShoulder(self, value):
        if value<0:
            self.state.startACW('shoulder')
        elif value>0:
            self.state.startCW('shoulder')
        else:
            self.state.stopCW('shoulder')
            self.state.stopACW('shoulder')

    def RotateElbow(self, value):
        if value<-1:
            self.state.startACW('elbow')
        elif value>-1:
            self.state.startCW('elbow')
        else:
            self.state.stopCW('elbow')
            self.state.stopACW('elbow')


    def RotateWrist(self, value):
        if value<-1:
            self.state.startACW('wrist')
        elif value>-1:
            self.state.startCW('wrist')
        else:
            self.state.stopCW('wrist')
            self.state.stopACW('wrist')

    def SwitchLight(self, value):
        if value == 1:
            self.state.startCW('light')
        else:
            self.state.stopCW('light')
    
    def OpenGrip(self, value):
        if value == 1:
            self.state.startCW('grip')
        else:
            self.state.stopCW('grip')

    def CloseGrip(self, value):
        if value == 1:
            self.state.startACW('grip')
        else:
            self.state.stopACW('grip')
