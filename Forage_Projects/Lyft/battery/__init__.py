from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class Battery(SpindlerBattery, NubbinBattery):
    def needs_service(self):
        if SpindlerBattery.battery_should_be_serviced(self) and \
                NubbinBattery.battery_should_be_serviced(self):
            return True
        else:
            return False
