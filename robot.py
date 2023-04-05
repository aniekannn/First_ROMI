import wpilib
import os
from wpilib import TimedRobot, Joystick
from drivetrain import Drivetrain


class MyRobot(TimedRobot):

    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the joysticks and other presets.'''
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain()

    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''

    pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''
        pass

    def autonomousPeriodic(self):
        '''This is called every cycle while the robot is in autonomous.'''
        pass

    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass

    def teleopPeriodic(self):
        '''This is called once every cycle during Teleop'''
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.move(forward, rotate)
        print(forward)

    ### There are other methods that you can overwrite for when the robot is
    # disabled, or when the robot is in Test mode.

if __name__ == "__main__":
# If your ROMI isn't at the default address, set that here
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)

# after connect by wifi to romi, open web browser and type 10.0.0.2, click romi option from menu and click writable,
#dio channel 8, change to dio (channel 9),
