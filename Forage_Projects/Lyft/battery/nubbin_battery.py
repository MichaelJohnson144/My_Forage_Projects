from datetime import datetime

from car import Car
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class NubbinBattery(Car, Rorschach, Thovex):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = None
        rorschach = Rorschach(last_service_date, current_mileage, last_service_mileage)
        thovex = Thovex(last_service_date, current_mileage, last_service_mileage)

        if car == rorschach:
            if last_service_date == today.replace(year=today.year - 5):
                return last_service_date > self.current_date and \
                       rorschach.needs_service() is True
            elif last_service_date == today.replace(year=today.year - 3):
                return last_service_date < self.current_date and \
                       rorschach.needs_service() is False

        elif car == thovex:
            if last_service_date == today.replace(year=today.year - 5):
                return last_service_date > self.current_date and \
                       thovex.needs_service() is True
            elif last_service_date == today.replace(year=today.year - 3):
                return last_service_date < self.current_date and \
                       thovex.needs_service() is False
