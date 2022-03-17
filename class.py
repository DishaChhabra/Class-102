class Rectangle:
    # __init__ is the same as constructor
    def __init__(self,l,b):
        #this. = self.
        self.l = l
        self.b = b
    def move(self):
        print('function move called')
    def speed(self, s):
        print('the speed is',s)

rect = Rectangle(40,20)
print(rect.b)
rect.move()
rect.speed(90)

class Car:
    def __init__(self, speed, model, color):
        self.speed = speed
        self.model = model
        self.color = color
    def details(self):
        print('the details are :', self.speed, self.model, self.color)
    def company(self, name):
        print('the car belongs to', name)

car = Car(90,19036,'black')
car.details()
car.company('tata')

class ATM:
    def __init__(self, cardNum, pin, balance):
        self.cardNumber = cardNum
        self.cardPin = pin
        self.balance = balance
    def withdraw(self, amount):
        print('money withdrawn =', amount)
        print('money left =', self.balance-amount)

atm = ATM(192739203, 1234, 9000)
atm.withdraw(2000)