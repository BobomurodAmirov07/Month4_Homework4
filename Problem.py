class Car:
    def __init__(self, brand, year, color, mileage, petrol, petrol_box):
        self.brand = brand
        self.year = year
        self.color = color
        self.engine = False
        self.__mileage = mileage
        self.__petrol = petrol
        self.petrol_box = petrol_box
        self.needed_petrol = int()

    def switch_on(self):
        if self.engine == False:
            self.engine = True
            print("Car is switched on")
        else:
            print("Car is already switched on")

    def switch_off(self):
        if self.engine == True:
            self.engine = False
            print("Car is switched off")
        else:
            print("Car is already switched off")

    def fill_petrol(self, needed_petrol, money):
        m = 0
        for i in range(needed_petrol):
            money -= 10000
            self.__petrol += 1
            m += 1
        print(f"{needed_petrol} litr benzin to'ldirildi va {m} cha pulingiz ketdi\nQolgan pul {money}")

    def move(self, km, obj):
        if self.engine == True:
            if self.__petrol >= km:
                for i in range(km):
                    self.__petrol -= 1
                    self.__mileage += 1
                print(f"Manzilga yetib keldinggiz {km} km yurdingiz va {self.__petrol} litr benziningiz qoldi")
            else:
                print(f"Sizga {km - self.__petrol} litr benzin yetmayabdi")
                s = input("1 litr benzin narxi 10000\nBenzin to'ldirishni hohlaysizmi\nHa -> 1\nYo'q -> 2\n>>> ")
                self.needed_petrol = km - self.__petrol
                if s == '1' and obj.money >= self.needed_petrol:
                    self.fill_petrol(self.needed_petrol, obj.money)
                    self.move(km, obj)
                else:
                    print("Yo'liz shuyerda tugadi")
        else:
            self.switch_on()
            self.move(km, obj)


class Person(Car):
    def __init__(self, name, money, obj : Car):
        self.name = name
        self.money = money
        self.car = obj

    def fill(self, km, obj):
        self.car.move(km, obj)
    


c1 = Car("Nissan", 2022, "Silver", 10000, 40, 60)
p1 = Person("John", 540000, c1)

p1.fill(50, p1)