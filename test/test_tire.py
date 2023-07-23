import unittest

from components.tire import CarriganTire, OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_array = [0.9, 0.8, 0.8, 0.8]  # Needs service
        tire = CarriganTire(tire_wear_array)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_array = [0.8, 0.8, 0.8, 0.8]  # No service needed
        tire = CarriganTire(tire_wear_array)

        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_array = [1, 1, 1, 0]  # Needs service
        tire = OctoprimeTire(tire_wear_array)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_array = [0.5, 0.5, 0.5, 0.5]  # No service needed
        tire = OctoprimeTire(tire_wear_array)

        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
