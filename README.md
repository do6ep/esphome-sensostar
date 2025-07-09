# esphome-sensostar

**Custom ESPHome Component for Engelmann SensoStar Heat Meters**

This ESPHome integration enables reading detailed heat consumption data from Engelmann SensoStar M-Bus heat meters and makes it available in Home Assistant.

---

## 🔧 Features

- 📊 **Sensor Readings**
  - Energy consumption (kWh)
  - Flow rate (m³/h)
  - Volume (m³)
  - Power (W)
  - Flow temperature (°C)
  - Return temperature (°C)
  - Temperature difference (ΔT)
  - Meter status (text)
  - Battery voltage (via ADC)

- 🧠 **Home Assistant Integration**
  - Native API support
  - OTA updates
  - Web dashboard (optional)

- 🕹 **Controls**
  - Template button in Home Assistant for instant battery reading

- 💡 **LED Indicators**
  - Flash programming
  - Wi-Fi connection status
  - Heartbeat (device activity)
  - New data received from the SensoStar meter

---

## 🧪 Requirements

- ESP32-S3 DevKitC-1 (8MB Flash, with PSRAM)
- Engelmann SensoStar meter with M-Bus interface
- ESPHome installed on your system
- Home Assistant (optional but recommended)

---

## 🚀 Setup Instructions

1. **Install ESPHome**  
   [ESPHome installation guide](https://esphome.io/guides/installing_esphome.html)

2. **Clone or reference this repository** in your ESPHome config:
   ```yaml
   external_components:
     - source:
         type: git
         url: https://github.com/STB3/esphome-sensostar
       components: [ SensoStar_MBus ]
   ```

3. **Create a `secrets.yaml` file** in the same folder as your ESPHome config file (`sensostar.yaml`):

   ```yaml
   # secrets.yaml
   wifi_ssid: "YourSSID"
   wifi_password: "YourPassword"
   api_encryption_key: "YourAPIKey"  # Generate with: openssl rand -base64 32
   ```

4. **Build and upload your firmware:**
   ```bash
   cd path\to\your\config
   esphome run sensostar.yaml
   ```

---

## 📦 Repository Contents

- `components/SensoStar_MBus/`: Custom ESPHome component for the SensoStar M-Bus meter
- No user-specific configuration files are committed (e.g. `sensostar.yaml` or `secrets.yaml`)

---

## 🔐 Security Note

This repository **does not** contain any private configurations. Be sure to:
- Use `secrets.yaml` to keep credentials out of your main config
- Add `.gitignore` rules to exclude secrets from being committed

```gitignore
# .gitignore
secrets.yaml
*.key
*.pem
```

---

## 📫 Contact

Maintained by **STB3**  
For issues or feature requests, open an issue in the [GitHub repository](https://github.com/STB3/esphome-sensostar/issues).

---

## 📝 License

This project is open-source and licensed under the MIT License.
