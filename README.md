# eink-tools

Here are some projects using the DFRobot eink display, primarily with a raspberry pi zero 2 w. Dietpi with a minimal install was used. Using `dietpi-software`, git (17), Python 3 (130), Python 3-GPIO (69) were installed.

Add `dtparam=spi=on` to config.txt

### Display library
Requires DFRobot display library. The [original library](https://github.com/cdjq/DFRobot_RPi_Display_V3) has some discrepancies as of 3/11/2023 and a [corrected version was made with some minor modifications](https://github.com/dabernards/DFRobot_RPi_Display_V3).

### Dependencies
Yaml is used for settings. QR code used to generate the QR code and pillow to convert the png to a bmp

`pip install pyyaml qrcode pillow`

`sudo apt install python3-spidev python3-freetype fonts-dejavu-core`


### Use
Run `python3 wifi-qr.py` (currently requires running as root, should be able to add user to gpio or dialout group to give user priviledge to GPIO pins, but have yet to check/test)

If auto-refresh is desired, the systemd service can be addd. Copy `wifi-qr.service` to `/etc/systemd/system/` and enable the service with `sudo systemctl enable wifi-qr`
