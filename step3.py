class Car:
    def __init__(self, mark, speed):
        self.mark = mark
        self.speed = speed

    def incr_speed(self):
        self.speed = self.speed + self.speed
        return self.speed


car1 = Car("BMV", 30)
print('Вы увеличили скорость до', car1.incr_speed())
