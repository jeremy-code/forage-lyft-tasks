import unittest
from datetime import datetime
from components.battery import SpindlerBattery, NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)

        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date, today)

        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
