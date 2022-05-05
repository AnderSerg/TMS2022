from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def __init__(self, label: str = '', color: str = 'black'):
        self.label = label
        self.color = color
        self.max_speed = 200
        self.current_speed = 0

    def info(self):
        """Информация о машине"""
        print(f'Я - машина "{self.label}".\n'
              f'У меня цвет - {self.color}\n'
              f'Моя максимальная скорость {self.max_speed}км/ч\n'
              f'Я еду со скоростью {self.current_speed}км/ч')

    def stop(self):
        """Остановить машину"""
        self.current_speed = 0
        print("Машина Остановлена")

    @abstractmethod
    def drive(self, add_speed: int):
        """Увеличение скорости"""
        self.current_speed = min((self.current_speed + add_speed, self.max_speed))
        print(f'Теперь я еду со скоростью {self.current_speed}км/ч')


class VolksWagenCar(Car):
    def __init__(self, label: str = 'VolksWagen', color: str = 'Red'):
        self.label = label
        self.color = color
        self.max_speed = 300
        self.current_speed = 0

    def drive(self, add_speed: int):
        self.current_speed = min((self.current_speed + add_speed + 10, self.max_speed))
        print(f'Теперь я еду со скоростью {self.current_speed}км/ч')

    def speed_limit(self):
        if self.current_speed > 150:
            print(f'Опасная скорость для {self.label}')


class AudiCar(Car):
    def __init__(self, label: str = 'Audi', color: str = 'Green'):
        self.label = label
        self.color = color
        self.max_speed = 400
        self.current_speed = 0

    def drive(self, add_speed: int):
        self.current_speed = min((self.current_speed + add_speed + 20, self.max_speed))
        print(f'Теперь я еду со скоростью {self.current_speed}км/ч')

    def cruise_control(self, new_speed: int):
        self.current_speed = new_speed
        print(f'Текущая скорость установленная в круиз контроле{self.current_speed}')


class Airplane(ABC):
    @abstractmethod
    def __init__(self, label: str = '', color: str = 'Silver'):
        self.label = label
        self.color = color
        self.max_speed = 2000
        self.current_speed = 0

        self.max_height = 10000
        self.current_height = 0

    def info(self):
        """Информация о самолёте"""
        print(f'Я - самолёт "{self.label}".\n'
              f'У меня цвет - {self.color}\n'
              f'Моя максимальная скорость {self.max_speed}км/ч\n'
              f'Моя максимальная высота {self.max_height}м\n'
              f'Я лечу со скоростью {self.current_speed}км/ч\n'
              f'Я лечу на высоте {self.current_height}м'
              )

    @abstractmethod
    def drive_fly(self, add_speed: int):
        """Увеличение скорости"""
        self.current_speed = min((self.current_speed + add_speed, self.max_speed))
        print(f'Теперь я еду со скоростью {self.current_speed}км/ч')

    @abstractmethod
    def fly(self, add_height: int):
        self.current_height = min(self.current_height + add_height, self.max_height)
        print(f'Теперь я лечу на высоте {self.current_height}м')


class AirBus(Airplane):
    def __init__(self, label: str = 'AirBus', color: str = 'Black'):
        self.label = label
        self.color = color
        self.max_speed = 2000
        self.current_speed = 0

        self.max_height = 10000
        self.current_height = 0

    def drive_fly(self, add_speed: int):
        """Увеличение скорости"""
        self.current_speed = min((self.current_speed + add_speed + 100, self.max_speed))
        print(f'Теперь я еду со скоростью {self.current_speed}км/ч')

    def fly(self, add_height: int):
        """Увеличение высоты"""
        self.current_height = min(self.current_height + add_height + 500, self.max_height)
        print(f'Теперь я лечу на высоте {self.current_height}м')


def main():

    car1_vw = VolksWagenCar()
    car1_vw.info()

    print()

    car1_vw.current_speed = 15
    car1_vw.info()

    print()

    car1_vw.drive(59)
    car1_vw.info()

    print()

    car1_vw.drive(59)
    car1_vw.info()
    car1_vw.speed_limit()

    print()
    print()
    print()

    car2_audi = AudiCar()
    car2_audi.info()

    print()

    car2_audi.drive(59)
    car2_audi.info()

    print()

    car2_audi.drive(59)
    car2_audi.info()

    print()
    print()
    print()

    airplane_1 = AirBus()
    airplane_1.info()

    print()

    airplane_1.current_height = 1000
    airplane_1.info()

    print()

    airplane_1.drive_fly(500)
    airplane_1.fly(1000)


if __name__ == '__main__':
    main()
