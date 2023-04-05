from wpilib import DigitalInput

class LineFollower:

    def __init__(self, drivetrain):
        self.left_sensor = DigitalInput(8)
        self.right_sensor = DigitalInput(9)
        self.drivetrain = drivetrain
        # 8 and 9 are important here

    def run(self):
        left_data = self.left_sensor.get()
        right_data = self.right_sensor.get()

    # logic and motor setting.