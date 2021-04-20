import time


class TrafficLight:

    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            print(self.__color)
            TrafficLight.show_timer(7)
            self.__color = "yellow"
            print(self.__color)
            TrafficLight.show_timer(2)
            self.__color = "green"
            print(self.__color)
            TrafficLight.show_timer(3)
            self.__color = "red"

    @staticmethod
    def show_timer(sec: int):
        for ind in range(sec):
            time.sleep(1)
            if ind + 1 > (sec - 1):
                end = '\n'
            else:
                end = ''
            print(' ', ind + 1, end=end)
        time.sleep(1)


traffic_light = TrafficLight()
traffic_light.running()
