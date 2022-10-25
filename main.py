import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 30
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep!")
        self.gladness += 3

    def to_work(self):
        print("job")
        self.money += 40
        self.gladness -= 5

    def to_chill(self):
        print("Rest time!")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 20

    def Ispravlenie(self):
        if self.progress < -0.5:
            print("Game over")
            self.to_study()
        elif self.gladness <= 0:
            print("Ded inside")
            self.to_chill()
        elif self.money <= 5:
            print("Bomj")
            self.to_work()

    def end_of_day(self):
        print("Gladness:", self.gladness)
        print("Progress:", self.progress)
        print("Money:", self. money)

    def live(self, day):
        print("Day", str(day), "of", self.name, "live")
        num = random.randint(1, 4)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()
        elif num == 4:
            self.to_work()

        self.end_of_day()
        self.Ispravlenie()


nick = Student("nick")
for day in range(366):
    if nick.alive == False:
        break
    nick.live(day)