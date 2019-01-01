import usb.core, usb.util, time

class Motor:
    def __init__(self, cw_flag, acw_flag, off_flag):
        self.clockwise = False
        self.anticlockwise = False
        self.cw_flag = cw_flag
        self.acw_flag = acw_flag
        self.off_flag = off_flag

    def isTurningCW(self):
        return self.clockwise

    def isTurningACW(self):
        return self.anticlockwise

    def startACW(self):
        if self.isTurningCW():
            self.stopCW()
        self.anticlockwise = True
        
    def stopACW(self):
        self.anticlockwise = False

    def startCW(self):
        if self.isTurningACW():
            self.stopACW()
        self.clockwise = True
        
    def stopCW(self):
        self.clockwise = False
        
    def render(self):
        if self.clockwise:
            return self.cw_flag
        elif self.anticlockwise:
            return self.acw_flag
        else:
            return self.off_flag

class Owi535State:

    def __init__(self):
        self.flags      = [0, 0, 0]
        self.components = {
            '''light''':    Motor([0,0,1],[0,0,0],[0,0,0]),
            '''base''':     Motor([0,1,0],[0,2,0],[0,0,0]),
            '''shoulder''': Motor([64,0,0],[128,0,0],[0,0,0]),
            '''elbow''':    Motor([16,0,0],[32,0,0],[0,0,0]),
            '''wrist''':    Motor([4,0,0],[8,0,0],[0,0,0]),
            '''grip''':     Motor([1,0,0],[2,0,0],[0,0,0])
        }


    def render(self):
        flags = [0, 0, 0]
        for key,c in self.components.iteritems():
            ArmCmd = c.render()
            flags[0] |= ArmCmd[0]
            flags[1] |= ArmCmd[1]
            flags[2] |= ArmCmd[2]
        return flags

    def startACW(self, component):
        self.components[component].startACW()

    def stopACW(self, component):
        self.components[component].stopACW()

    def isTurningACW(self, component):
        return self.components[component].isTurningACW()

    def startCW(self, component):
        self.components[component].startCW()

    def stopCW(self, component):
        self.components[component].stopCW()

    def isTurningCW(self, component):
        return self.components[component].isTurningCW()

