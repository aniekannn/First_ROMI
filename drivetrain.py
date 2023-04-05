import os
from wpilib import Spark
from wpilib.drive import DifferentialDrive


class Drivetrain:
    def __init__(self):
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.right_motor, self.left_motor)

    def move(self, rotate, forward):
        self.drivetrain.arcadeDrive(rotate, forward)
