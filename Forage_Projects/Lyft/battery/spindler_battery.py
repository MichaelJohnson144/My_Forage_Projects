from datetime import datetime

from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome


class SpindlerBattery(Car, Palindrome, Glissade):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int
        warning_light_is_on = bool

        car = None
        calliope = Calliope(last_service_date, current_mileage, last_service_mileage)
        glissade = Glissade(last_service_date, current_mileage, last_service_mileage)
        palindrome = Palindrome(last_service_date, warning_light_is_on)

        if car == calliope:
            if last_service_date == today.replace(year=today.year - 3):
                return last_service_date > self.current_date and \
                       calliope.needs_service() is True
            elif last_service_date == today.replace(year=today.year - 1):
                return last_service_date < self.current_date and \
                       calliope.needs_service() is False

        elif car == glissade:
            if last_service_date == today.replace(year=today.year - 3):
                return last_service_date > self.current_date and \
                       glissade.needs_service() is True
            elif last_service_date == today.replace(year=today.year - 1):
                return last_service_date < self.current_date and \
                       glissade.needs_service() is False

        elif car == palindrome:
            if last_service_date == today.replace(year=today.year - 5):
                return last_service_date > self.current_date and \
                       palindrome.needs_service() is True
            elif last_service_date == today.replace(year=today.year - 3):
                return last_service_date < self.current_date and \
                       palindrome.needs_service() is False
