import unittest
from datetime import datetime
from components.engine import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage
        )

        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage
        )

        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = SternmanEngine(last_service_date, warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        engine = SternmanEngine(last_service_date, warning_light_is_on)

        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
