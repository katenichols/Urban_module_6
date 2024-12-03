import random


class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self):
        _cords = [0, 0, 0]
        speed = ...

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = dz * self.speed


    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        count_of_eggs = random.randint(1, 5)
        if count_of_eggs == 1:
            print(f"Here is {count_of_eggs} eggs for you")
        else:
            print(f"Here are {count_of_eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        super()._cords[2] = abs(super()._cords[2]) * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)