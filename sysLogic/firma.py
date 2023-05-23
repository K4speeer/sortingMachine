# For running this script should use dgtEnv enviroment because of used python version 
from pymata4 import pymata4
import time 
import asyncio

board = pymata4.Pymata4()

board.set_pin_mode_digital_output(13)
board.get_analog_map()
board.get_capability_report()
board.get_firmware_version()
board.get_protocol_version()
board.get_pymata_version()

try:
    while True:
        board.digital_write(13,1)
        time.sleep(2)
        board.digital_write(13,0)
        time.sleep(1)

except KeyboardInterrupt:
    board.shutdown()
    exit()