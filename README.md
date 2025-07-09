# esphome-sensostar
Custom ESPHome component use with SensoStar module

Provides the data from a Engelmann SensoStar heat meter to HomeAssitant

Supported readings:
- Voltage level of the internal battery
- Energy {kWh]
- Flow [m³/h]
- Flow temperature °C
- Return temperature °C
- Power [W]
- Temperature difference in/out
- Volume [m³]
- Status

Button for reading the internal battery in Homeassistant instantaneously

4 LEDs indicating:
- Flash programming
- WiFi connected
- Heartbeat
- New data from Sensostar heat meter

HowTo build:
- Install ESPHome
- Open CMD line
- Enter the directory where sensostar.yaml is located
- Type: esphome run sensostar.yaml

