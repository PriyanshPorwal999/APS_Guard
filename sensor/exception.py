import sys
import os

class SensorException(Exception):

    def __init__(self, error_message, error_details: sys):

        super().__init__(error_message)

    def __str__(self):
        return super().error_message    