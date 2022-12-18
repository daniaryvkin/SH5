import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness += self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Happy!')
            self.gladness += 10
            self.money -= 15
            self.satiety += 5

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clear_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength = 100
        self.money -= 50

    def indexes_day(self, day):
        day = f'Today the {day} of {self.name} life'
        print(f'{day:+^50}')
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}")
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')
        car_indexes = f'{self.car.brand} car indexes'
        print(f'{car_indexes:^50}')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

    def is_alive(self):
        if self.gladness <= 0:
            print('Depression')
            return False
        if self.satiety <= 0:
            print('Dead....')
            return False
        if self.money < -200:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")
        self.indexes_day(day)
        dice = random.randint(1, 4)
        if self.satiety < 10:
            print('I go eat')
            self.eat()
        elif self.gladness < 10:
            if self.home.mess > 15:
                print('I want to chill, but there is si much mess ')
                self.clear_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 20:
            print('Start working!')
            self.work()
        elif self.car.strength < 10:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print("Let's chill")
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Cleaning time')
            self.clear_home()
        elif dice == 4:
            print('Time for treats!')
            self.shopping(manage='delicacies')


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move....')
            return False


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, "gladness_less": 10},
            'C++': {'salary': 80, "gladness_less": 5},
            'Python': {'salary': 30, "gladness_less": 8},
            'Rust': {'salary': 60, "gladness_less": 6}}

brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 15},
                'Lada': {'fuel': 70, 'strength': 20, 'consumption': 8},
                'Volvo': {'fuel': 90, 'strength': 150, 'consumption': 6},
                'Ford': {'fuel': 50, 'strength': 120, 'consumption': 12}}

nick = Human(name='Nick')

for day in range(1, 8):
    if nick.live(day) == False:
        break