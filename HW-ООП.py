import math

from abc import abstractmethod
from abc import ABC


# Задание № 1. Инкапсуляция
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        try:
            if amount > self.__balance:
                raise ValueError('Недостаточно средств')
            self.__balance -= amount
        except ValueError as e:
            print(f"Ошибка: {e}")



    def get_balance(self):
        return self.__balance

A = BankAccount(1000)
A.deposit(500)


# Задание № 2. Наследование
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}'

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, 'Developer', salary)
        self.programming_language=programming_language

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Язык программирования: {self.programming_language}'

class Manager(Employee):
    def __init__(self, name, salary, employees):
        super().__init__(name, 'Менеджер', salary)
        self.employees = employees


    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Список сотрудников: {self.employees}'



# Задание № 3. Полиморфизм

class Shape:
    def area(self):
        pass

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return self.radius * (2 * math.pi)


# Задание № 4. Абстракция и интерфейс

class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def start_engine(self):
        return "Двигатель заведен"

    def stop_engine(self):
        return 'Двигатель заглушен'

    def move(self):
        return 'Автомобиль движется'


class Boat(Transport):
    def start_engine(self):
        return "Двигатель лодки заведен"

    def stop_engine(self):
        return 'Двигатель лодки заглушен'

    def move(self):
        return 'Лодка движется'


# Задание № 5. Множественное наследование

class Flyable:
    def fly(self):
        return 'Im flying'

class Swimmable:
    def swim(self):
        return "I'm swimming"

class Duck(Flyable, Swimmable):
    def make_sound(self):
        return "Quack"

x = Duck()
# print(x.fly(), x.swim(), x.make_sound())

# Задание № 6. Комбинированное

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

    def move(self):
        return "Бегает"

class Bird(Animal, Flyable):
    def speak(self):
        return "Tweet"

    def move(self):
        return Flyable.fly(self)

class Fish(Animal, Swimmable):
    def speak(self):
        return "Молчит"

    def move(self):
        return Swimmable.swim(self)

list_animals = [Dog(), Bird(), Fish()]

# for animal in list_animals:
    # print(animal.speak())
    # print(animal.move())
    # print('----')


# Singleton
class Logger:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.logs = []
        return cls.instance

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs


logger1 = Logger()
logger2 = Logger()

# logger1.log("First message")
# logger2.log("Second message")
#
#
# assert logger1 is logger2, "Logger is not a singleton!"
# assert logger1.get_logs() == ["First message", "Second message"]


# SOLID (S)

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content



class PDFgenerator:
    def generate_pdf(self):
        print(f"PDF generated report")


class FileSaver:
    def save_to_file(self, filename):
        print(f"Saved {filename}")



# report = Report('Заголовок', 'Отчет')
#
# pdf_generator = PDFgenerator()
# print(pdf_generator.generate_pdf())

# SOLID (O)

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(PaymentProcessor):
    def pay(self):
        return "Оплата прошла через PayPal"

class CreditCard(PaymentProcessor):
    def pay(self):
        return "Оплачено кредитной картой"

class Crypto(PaymentProcessor):
    def pay(self):
        return "Оплачено криптой"


# SOLID (L)
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def __init__(self, name):
        self.name = name

    def fly(self):
        return "Умеет летать"

class Penguin(Bird):
    def __init__(self, name):
        self.name = name

    def fly(self):
        return "Не умеет летать"


# SOLID (I)

class Animal_fly(ABC):
    @abstractmethod
    def fly(self):
        pass

class Animal_run(ABC):
    @abstractmethod
    def run(self):
        pass

class Animal_swim(ABC):
    @abstractmethod
    def swim(self):
        pass

class Lion(Animal_run):
    def run(self):
        return "Лев умеет бегать"


# Декораторы класса

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def fahrenheit(cls, celsius):
        fahrenheit_1 = (celsius * 9) / 5 + 32
        return cls(fahrenheit_1)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(celsius):
        if celsius <= 0:
            return True
        else:
            return False
