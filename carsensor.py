from __main__ import UltraSonic

class CarSensor(UltraSonic):
    def __init__(self, *args, **kwargs):
        print("Initializing CarSensor")
        super().__init__(*args, **kwargs)

    def send_distance(self):
        distance = self.sensor.distance_cm()
        if hasattr(self.parent, "mqtt"):
            self.parent.mqtt.publish("hacklab/"+self.parent.mqtt.settings["client_name"]+"/carsensor_value", str(distance), False)

    def mqtt_on_connect_callback(self, **kwargs):        
        self.send_distance()

    def before_deepsleep_callback(self,*args,**kwargs):
        self.send_distance()
