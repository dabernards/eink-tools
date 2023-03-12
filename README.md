# eink-tools

Here are some projects using the DFRobot eink display, primarily with a raspberry pi zero 2 w. Dietpi with a minimal install was used. Using `dietpi-software`, git (17), Python 3 (130), Python 3-GPIO (69) were installed.

Add `dtparam=spi=on` to config.txt

### Display library
Requires DFRobot display library. The [original library](https://github.com/cdjq/DFRobot_RPi_Display_V3) has some discrepancies as of 3/11/2023 and a [corrected version was made with some minor modifications](https://github.com/dabernards/DFRobot_RPi_Display_V3).

### Dependencies
Yaml is used for settings. QR code used to generate the QR code and pillow to convert the png to a bmp
`pip install pyyaml qrcode pillow`

### Use
Added `python3 wifi-qr.py` to /etc/rc.local to ensure display is present on boot up.
