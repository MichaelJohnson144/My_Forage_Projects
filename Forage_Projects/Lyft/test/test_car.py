import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_service_criteria(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == today.replace(year=today.year - 3):
                return self.assertTrue(car.needs_service())
            elif last_service_date == today.replace(year=today.year - 1):
                return self.assertFalse(car.needs_service())

    def test_engine_service_criteria(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 30000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 30000:
                return self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_service_criteria(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == today.replace(year=today.year - 3):
                return self.assertTrue(car.needs_service())
            elif last_service_date == today.replace(year=today.year - 1):
                return self.assertFalse(car.needs_service())

    def test_engine_service_criteria(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 60000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 60000:
                return self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_service_criteria(self):
        today = datetime.today().date()
        last_service_date = None
        warning_light_is_on = bool

        car = Palindrome(last_service_date, warning_light_is_on)
        if car == car:
            if last_service_date == today.replace(year=today.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == today.replace(year=today.year - 3):
                return self.assertFalse(car.needs_service())

    def test_engine_service_criteria(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = bool

        car = Palindrome(last_service_date, warning_light_is_on)
        if warning_light_is_on is True:
            return self.assertTrue(car.needs_service())
        elif warning_light_is_on is False:
            return self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_service_criteria(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == today.replace(year=today.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == today.replace(year=today.year - 3):
                return self.assertFalse(car.needs_service())

    def test_engine_service_criteria(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 60000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 60000:
                return self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_service_criteria(self):
        today = datetime.today().date()
        last_service_date = None
        current_mileage = int
        last_service_mileage = int

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if last_service_date == today.replace(year=today.year - 5):
                return self.assertTrue(car.needs_service())
            elif last_service_date == today.replace(year=today.year - 3):
                return self.assertFalse(car.needs_service())

    def test_engine_service_criteria(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        if car == car:
            if current_mileage >= 30000:
                return self.assertTrue(car.needs_service())
            elif current_mileage < 30000:
                return self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
