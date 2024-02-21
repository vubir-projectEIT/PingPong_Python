from serial import Serial
from time import sleep

class Controller:

    def __init__(self):
        self.connection = Serial('/dev/cu.usbserial-A10JV57T')

    def set_setpoint(self, value: int) -> None:
        if self.connection.is_open:
            self.connection.write(f'S{value}\r\n'.encode('utf-8'))
            response = self.connection.readline()
            print(response)

if __name__ == "__main__":

    controller = Controller()

    while True:
        controller.set_setpoint(255)
        sleep(20)
        controller.set_setpoint(60)
        sleep(20)
        controller.set_setpoint(255)