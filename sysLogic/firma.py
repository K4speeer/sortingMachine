# For running this script should use dgtEnv enviroment because of used python version 
from pyfirmata import ArduinoNano



if __name__ == "__main__":
    board = ArduinoNano("/dev/ttyUSB0", baudrate=9600)
    print("communication successfully started !!!")

    led = board.digital[13]

    while True:
        led.write(1)
        board.pass_time(1)
        led.write(0)
        board.pass_time(1)
