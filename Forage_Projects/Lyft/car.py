from engine.__init__ import Engine
from battery.__init__ import Battery


class Car(Engine, Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self):
        if self.engine.needs_service() and self.battery.needs_service():
            return True
        else:
            return False
