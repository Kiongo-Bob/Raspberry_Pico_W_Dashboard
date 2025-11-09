# Raspberry Pi Pico Data Telemetry using a Low Code and Custom Code approach

## Low Code Approach
This uses existing tools to implement a reporting dashboard for sensor data from the Raspberry Pi Pico.
Tech stack:
- MQTT Communication protocol
- **Hardware**: Raspberry Pi Pico W
- **Firmware layer**: MicroPython: (Low code implementation)
- **Backend**: Node-RED (Runs on top of NodeJS)
- **UI**: Grafana Dashboard
- **Endpoints**: Pub-Sub topics
- **Security**: TLS Encryption

## Custom Code Approach
This approach builds the Full stack app from scratch. From the data source to the reporting dashboard for sensor data from the Raspberry Pi Pico.
Tech stack:
- MQTT Communication protocol
- **Hardware**: Raspberry Pi Pico W
- **Firmware layer**: C (Custom code implementation)
- **Backend**: NodeJS
- **UI**: REACT
- **Endpoints**: Mosquitto (Pub-Sub topics)
- **Security**: TLS Encryption