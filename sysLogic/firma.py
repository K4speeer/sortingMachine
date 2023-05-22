# For running this script should use dgtEnv enviroment because of used python version 
from pyfirmata import ArduinoNano



if __name__ == "__main__":
    board = ArduinoNano("/dev/ttyUSB0", baudrate=9600)
    print("communication successfully started !!!")

    #Defining IR sensor port 
    # ir_sensor = board.digital[]

    #Defining PCA-9685 pins to connect with arduino

    #Defining Stepper motor shield pins

    