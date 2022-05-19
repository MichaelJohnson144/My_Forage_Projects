from battery.battery import Battery


# In order for concrete/child/subclass "SpindlerBattery" to "'instantiate' the 'abstract parent/base class 'Battery,''
# its 'parent class' ''must' be called.'"

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        pass
