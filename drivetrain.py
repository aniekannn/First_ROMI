import os
from wpilib import Spark
from wpilib.drive import DifferentialDrive


class Drivetrain:
    def __init__(self):
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.right_motor, self.left_motor)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward, rotate)


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)