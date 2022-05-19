import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_engine_service_criteria(self):
        current_date = None
        last_service_date = None
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 30000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 30000:
                return self.assertFalse(car.needs_service())

    def test_battery_service_criteria(self):
        current_date = datetime.today().date()
        last_service_date = None
        current_mileage = None
        last_service_mileage = None

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == current_date.replace(year=current_date.year - 3):
                return self.assertTrue(car.needs_service())
            elif last_service_date == current_date.replace(year=current_date.year - 1):
                return self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_engine_service_criteria(self):
        current_date = None
        last_service_date = None
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 60000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 60000:
                return self.assertFalse(car.needs_service())

    def test_battery_service_criteria(self):
        current_date = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = CarFactory.glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == current_date.replace(year=current_date.year - 3):
                return self.assertTrue(car.needs_service())
            elif last_service_date == current_date.replace(year=current_date.year - 1):
                return self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_engine_service_criteria(self):
        current_date = None
        last_service_date = None
        warning_indicator_is_on = bool

        car = CarFactory.palindrome(current_date, last_service_date, warning_indicator_is_on)
        if warning_indicator_is_on is True:
            return self.assertTrue(car.needs_service())
        elif warning_indicator_is_on is False:
            return self.assertFalse(car.needs_service())

    def test_battery_service_criteria(self):
        current_date = datetime.today().date()
        last_service_date = None
        warning_indicator_is_on = bool

        car = CarFactory.palindrome(current_date, last_service_date, warning_indicator_is_on)
        if car == car:
            if last_service_date == current_date.replace(year=current_date.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == current_date.replace(year=current_date.year - 3):
                return self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_engine_service_criteria(self):
        current_date = None
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 60000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 60000:
                return self.assertFalse(car.needs_service())

    def test_battery_service_criteria(self):
        current_date = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == current_date.replace(year=current_date.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == current_date.replace(year=current_date.year - 3):
                return self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_engine_service_criteria(self):
        current_date = None
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 30000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 30000:
                return self.assertFalse(car.needs_service())

    def test_battery_service_criteria(self):
        current_date = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = CarFactory.calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == current_date.replace(year=current_date.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == current_date.replace(year=current_date.year - 3):
                return self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
