from battery import *
class Car:
    """Базовый класс автомобиля"""

    def __init__(self, marka, speed):
        '''Инициализирует атрибуты марки и скорости автомобиля'''
        self.marka = marka
        self.speed = speed
        self.odometr_reading = 0

    def car_ride(self, hours):
        amount = str(self.speed * hours)
        print( "Car has gone " + amount + " km ")
        return self.speed * hours

    def read_odometr(self):

        """Выведет нам пробег автомобиля """
        print("У этого автомобиля пробег " + self(self.odometr_reading) + "на счетчике")
    def update_odometr(self, km):
        self.odometr = km

class Tesla(Car):
    """Представляет класс автомобилей с электродвигателем"""
    def __init__(self, marka, speed):
        super().__init__(marka, speed)
        self.battery = Battery(120)
