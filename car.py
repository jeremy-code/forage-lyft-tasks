from components.battery import NubbinBattery, SpindlerBattery
from components.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from servicable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(
        last_service_date, current_mileage, last_service_mileage, current_date
    ):
        return Car(
            CapuletEngine(last_service_date, current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_glissade(
        last_service_date, current_mileage, last_service_mileage, current_date
    ):
        return Car(
            WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_palindrome(last_service_date, warning_light_is_on, current_date):
        return Car(
            SternmanEngine(last_service_date, warning_light_is_on),
            NubbinBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_rorschach(
        last_service_date, current_mileage, last_service_mileage, current_date
    ):
        return Car(
            WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_thovex(
        last_service_date, current_mileage, last_service_mileage, current_date
    ):
        return Car(
            CapuletEngine(last_service_date, current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )
