from pymata4 import pymata4
import time 
import asyncio



ir = 7 
innser_led = 13



def blink(value, board, pin):
    if value == 0:
        board.digital_write(pin, 1)
        time.sleep(.5)
        board.digital_write(pin, 0)
        time.sleep(.5)
    else:
        pass

def ir_listener(board, pin):
    def check_state(value):
        if value == 0:
            print("zero")
        else:
            print("one")
    
    try:
        while True:
            value, time_stamp = board.digital_read(ir)
            check_state(value)
            time.sleep(.5)
    except KeyboardInterrupt:
        board.shutdown()
        exit()


board = pymata4.Pymata4()

board.set_pin_mode_digital_output(innser_led)
board.set_pin_mode_digital_input(ir)


try:
    while True:
        ir_listener(board, ir)
except KeyboardInterrupt:
    board.shutdown()
    exit()

    



