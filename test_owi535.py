import unittest
from owi535state import Owi535State

class TestOwi535(unittest.TestCase):
    def setUp(self):
        self.arm = Owi535State()
    
    def checkLightOff(self):
        self.arm.stopCW("light")
        self.assertFalse(self.arm.isTurningCW("light"))

    def checkLightOn(self):
        self.arm.startCW("light")
        self.assertTrue(self.arm.isTurningCW('light'))

    def test_switch_light(self):
        self.assertFalse(self.arm.isTurningCW("light"))
        self.checkLightOn()
        self.checkLightOn()
        self.checkLightOff()
        self.checkLightOff()
        
    def test_base_acw(self):
        self.assertFalse(self.arm.isTurningACW('base'))
        self.arm.startACW('base')
        self.assertTrue(self.arm.isTurningACW('base'))
        self.arm.startACW('base')
        self.assertTrue(self.arm.isTurningACW('base'))
        self.arm.stopACW('base')
        self.assertFalse(self.arm.isTurningACW('base'))
        self.arm.stopACW('base')
        self.assertFalse(self.arm.isTurningACW('base'))
        
    def test_base_cw(self):
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.startCW('base')
        self.assertTrue(self.arm.isTurningCW('base'))
        self.arm.startCW('base')
        self.assertTrue(self.arm.isTurningCW('base'))
        self.arm.stopCW('base')
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.stopCW('base')
        self.assertFalse(self.arm.isTurningCW('base'))

    def test_base_acw_vs_light(self):
        self.assertFalse(self.arm.isTurningCW('light'))
        self.assertFalse(self.arm.isTurningACW('base'))
        self.arm.startACW('base')
        self.assertFalse(self.arm.isTurningCW('light'))
        self.assertTrue(self.arm.isTurningACW('base'))
        self.arm.startCW('light')
        self.assertTrue(self.arm.isTurningCW('light'))
        self.assertTrue(self.arm.isTurningACW('base'))
        self.arm.stopACW('base')
        self.assertTrue(self.arm.isTurningCW('light'))
        self.assertFalse(self.arm.isTurningACW('base'))
        self.arm.stopCW('light')
        self.assertFalse(self.arm.isTurningCW('light'))

    def test_base_acw_vs_cw(self):
        self.assertFalse(self.arm.isTurningACW('base'))
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.startACW('base')
        self.assertTrue(self.arm.isTurningACW('base'))
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.startCW('base')
        self.assertFalse(self.arm.isTurningACW('base'))
        self.assertTrue(self.arm.isTurningCW('base'))
        self.arm.startACW('base')
        self.assertTrue(self.arm.isTurningACW('base'))
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.stopCW('base')
        self.assertTrue(self.arm.isTurningACW('base'))
        self.assertFalse(self.arm.isTurningCW('base'))
        self.arm.stopACW('base')
        self.assertFalse(self.arm.isTurningACW('base'))
        self.assertFalse(self.arm.isTurningCW('base'))

    def test_render(self):
        self.assertEqual([0,0,0],self.arm.render())
        self.arm.startCW('light')
        self.assertEqual([0,0,1],self.arm.render())
        self.arm.startCW('light')
        self.assertEqual([0,0,1],self.arm.render())
        self.arm.startCW('wrist')
        self.assertEqual([4,0,1],self.arm.render())
        self.arm.stopCW('light')
        self.assertEqual([4,0,0],self.arm.render())
        self.arm.stopCW('light')
        self.assertEqual([4,0,0],self.arm.render())
        self.arm.stopCW('wrist')
        self.assertEqual([0,0,0],self.arm.render())
        self.arm.stopCW('wrist')
        self.assertEqual([0,0,0],self.arm.render())

if __name__ == '__main__': 
    unittest.main()
