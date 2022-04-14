from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class Engine(CapuletEngine, SternmanEngine, WilloughbyEngine):
    def needs_service(self):
        if CapuletEngine.engine_should_be_serviced(self) and \
                SternmanEngine.engine_should_be_serviced(self) and \
                WilloughbyEngine.engine_should_be_serviced(self):
            return True
        else:
            return False
