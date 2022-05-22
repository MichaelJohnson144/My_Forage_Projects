from tire.tire import Tire

import numpy as np


# For concrete/child/subclass "OctoprimeTires" to "'instantiate' the 'abstract parent/base class 'Tire,'' its 'parent
# class' ''must' be called.'"

class OctoprimeTires(Tire):
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.new_tire_wear_sensors = np.asfarray([self.x1, self.y1, self.x2, self.y2])

    def needs_service(self):
        return sum(self.new_tire_wear_sensors) >= 3
