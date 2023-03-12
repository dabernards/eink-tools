#!/bin/env python3
''' Code to write QR code and WiFi info 
    Depends on DFRobot Display library for eink display
    Importing the libraries isn't particularly graceful, 
    would be nice to improve this.

    Font ttf to use and WiFi details are read from settings.yml    
    '''

import sys
import qrcode
from PIL import Image as pimg
import yaml
# Need to add path of DFRobot display library
sys.path.append("../DFRobot_RPi_Display_V3") # set system path to top

#import time
# DFRobot libraries
from devices import DFRobot_Epaper
from display_extension.freetype_helper import Freetype_Helper

with open('settings.yml', 'r', encoding='utf-8') as f:
    settings = yaml.safe_load(f)

# Any fixed-width font should work here

qr = qrcode.QRCode(
    version=1,
    box_size=4,
    border=0,
)

qr.add_data(f"WIFI:S:{ settings['ssid'] };T:WPA;P:{ settings['password']};;")
qr_png = qr.make_image()
qr_png.save("qr-code.png")
qr_bmp = pimg.open("qr-code.png")
qr_bmp.save("qr-code.bmp")

# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4
RASPBERRY_PIN_RST = 26
epaper = DFRobot_Epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, \
		RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY,RASPBERRY_PIN_RST)


ft = Freetype_Helper(settings['fontFilePath'])
ft.setDisLowerLimite(112) # set display lower limit, adjust this to effect fonts color depth

# Initiate and clear screen
epaper.begin()
epaper.clearScreen()

epaper.setExFonts(ft) # init with fonts file
epaper.setTextFormat(1, epaper.BLACK, epaper.WHITE, 1, 1)

epaper.bitmapFile(0, 0, "./qr-code.bmp")

epaper.setExFontsFmt(20, 20) # set extension fonts width and height
epaper.setTextCursor(140,0)
epaper.printStr("SSID")
epaper.setExFontsFmt(24, 24) # set extension fonts width and height
epaper.setTextCursor(120,30)
epaper.printStr(f"{ settings['ssid'] }")
epaper.setTextCursor(140, 62)
epaper.setExFontsFmt(20, 20) # set extension fonts width and height
epaper.printStr("pwd (WPA)")
epaper.setExFontsFmt(22, 24) # set extension fonts width and height
epaper.setTextCursor(124, 94)
epaper.printStr(f"{settings['password']}")
for x in range(3):
    epaper.line(140, 22+x, 185, 22+x, epaper.BLACK)
    epaper.line(140, 84+x, 238, 84+x, epaper.BLACK)

epaper.flush(epaper.FULL)
