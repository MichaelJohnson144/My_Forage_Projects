from car import Car


class Serviceable(Car):
    def needs_service(self):
        if self.Car.needs_service():
            return True
        else:
            return False
