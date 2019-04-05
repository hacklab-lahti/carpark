# carpark
ESP32 Car park status sensor. Sends HC-SR04 -sensor value via MQTT and goes to deepsleep mode for specified time.

## External libraries

mPython-hcsr04 (https://pypi.org/project/mPython-hcsr04/)


## Install

1. Flash micropython firmware to your ESP32 (http://micropython.org/)
2. Rename settings-example.json to settings.json and modify at least wifi and mqtt server settings.
3. Upload files to ESP32 with adafruit-ampy (https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
4. Run install.py with ampy. It installs required libraries (ie. ampy -p /dev/tty.SLAB_USBtoUART run install.py)



## Implemented MQTT messages

**From node ->**
- hacklab/node_online (client_name)
- hacklab/client_name/carsensor_value (decimal value in cm)
