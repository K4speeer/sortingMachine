from pymata4 import pymata4
import time 
import asyncio



ir = 7 
innser_led = 13


unlock = 90
lock = 0
#First Gate Servo control 
def first_gate_servo(board, pin):
    global unlock
    global lock
    time.sleep(.5)
    board.servo_write(pin,unlock)
    time.sleep(1)
    board.servo_write(pin, lock)
    

# Blinker
def blink(value, board):
    if value == 0:
        board.digital_write(13, 1)
        time.sleep(.2)
        board.digital_write(13, 0)
        time.sleep(.2)
    else:
        pass

# Listener for IR-sensor value changes
def ir_listener(board, pin):
    def check_state(value):
        if value == 0:
            print("zero")
        else:
            print("one")
    
    try:
        while True:
            value, time_stamp = board.digital_read(pin)
            check_state(value)
            blink(value, board)
            first_gate_servo(board, 5)
            time.sleep(.2)
    except KeyboardInterrupt:
        board.shutdown()
        exit()




board = pymata4.Pymata4()

board.set_pin_mode_digital_output(innser_led)
board.set_pin_mode_digital_input(ir)
board.set_pin_mode_servo(5, 544, 2400)


try:
    while True:
        ir_listener(board, ir)
except KeyboardInterrupt:
    board.shutdown()
    exit()

    



