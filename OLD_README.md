This library (and its accompanying cli tool) is used to interface with
opple mobile-control lights.

## Supported Devices
All opple light with WIFI support (mobile control)

## Install
```bash
    pip install pyoppleio-legacy
```

## API Reference

class **OppleLightDevice**

*property:*
- **is_onlinee** [True|False] Readonly
- **power_on** [True|False] Read/Write
- **brightness** [10-255] Read/Write
- **color_temperature** [2700-6500] Read/Write

*method:*
- **__init__(ip)**
- **update()**

### Demo:
```python
    from pyoppleio.OppleLightDevice import OppleLightDevice
    
    light = OppleLightDevice('192.168.0.222')
    
    if not light.is_online:
        print('light is offline')
    elif not light.power_on:
        light.power_on = True
    else:
        light.brightness = 255
```

## CLI Command
-  search lights
   ```bash
   oppleio search
   ```
-  get one light's status
   ```bash
   oppleio get -a [light ip address]
   ```
-  turn on of turn off one light
   ```bash
   oppleio set -a [device ip address] -p on
   oppleio set -a [device ip address] -p off
   ````
-  set light's brightness and color temperature
   ```bash
   oppleio set -a [device ip address] -b 200 -c 4200
   ```