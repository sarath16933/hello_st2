from st2reactor.sensor.base import Sensor


class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)

    def setup(self):
        pass

    def run(self):
        self._logger.info('Hello world sensor')
        payload = {'greeting': 'Yo', 'count': 1}
        self.sensor_service.dispatch(trigger='hello_st2.event1', payload=payload)

    def cleanup(self):
        pass

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass