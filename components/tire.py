from abc import ABC
from servicable import Serviceable


class Tire(Serviceable, ABC):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array


class CarriganTire(Tire):
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear_array)


class OctoprimeTire(Tire):
    def needs_service(self):
        return sum(self.tire_wear_array) >= 3
