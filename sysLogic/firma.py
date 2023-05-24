'''
The projects logic is:
    1. Intro IR detects a ball 
    2. Start feeding the Cassette, using intro lilServo
'''
from pymata4 import pymata4
import time 
import asyncio

board = pymata4.Pymata4()

board.set_pin_mode_digital_output(13)
board.set_pin_mode_digital_input(7)


try:
    while True:
        board.digital_write(13,1)
        time.sleep(2)
        board.digital_write(13,0)
        time.sleep(1)

except KeyboardInterrupt:
    board.shutdown()
    exit()