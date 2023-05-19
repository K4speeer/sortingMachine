from pyfirmata import ArduinoNano
import time
import serial
import json
port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

if __name__ == "__main__":
    board = ArduinoNano("/dev/ttyUSB0", baudrate=9600 , timeout=1)
    print("communication successfully started !!!")

    while True:
        board.digital[13].write(1)
        time.sleep(4)
        board.digital[13].write(0)
        time.sleep(2)
