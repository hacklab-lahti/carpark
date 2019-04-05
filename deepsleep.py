from __main__ import Module
import machine

class DeepSleep(Module):
    def __init__(self, *args, **kwargs):
        print("Initializing DeepSleep")
        super().__init__(*args, **kwargs)

    def go_sleep(self):
        machine.deepsleep(self.settings["wakeup_after"])

    def mqtt_on_connect_callback(self, **kwargs):
        if self.settings["disable_autosleep"] == False:
            self.parent.call_callbacks("before_deepsleep_callback")
            self.go_sleep()