'''class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    
salary = int(input())
obj = Employee(salary)
obj.set_salary(salary)
print(obj.get_salary())'''

'''class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0      # private attribute

    def set_marks(self, m):
        if 0 <= m <= 100:
            self.__marks = m
            print("Marks updated!")
        else:
            print("Invalid marks! Enter between 0 and 100.")

    def get_marks(self):
        return self.__marks


# ---------- Runtime Input ----------
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s = Student(name)
s.set_marks(marks)

print("Student Name:", s.name)
print("Marks:", s.get_marks())'''

'''class Car:
    def __init__(self,brand):
        self.brand = brand
        self.__speed = 0

    def accelerate(self,value):
        if value>0:
            self.__speed+=value
            print(f"Accelerated by {value}")
        else:
            print("Invalid speed value!")

    def brake(self,value):
        if value>0:
            self.__speed-=value
            if self.__speed<0:
                self.__speed=0
            print(f"Braked by {value}")
        else:
            print("Invalid brake value")

    def get_speed(self):
        return self.__speed
    
brand = input()
obj = Car(brand)
acc = int(input())
obj.accelerate(acc)
br = int(input())
obj.brake(br)
print("Current Speed",obj.get_speed())'''


'''class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0      # private attribute

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
            print("Age updated successfully.")
        else:
            print("Invalid age! Enter a value between 0 and 120.")

    def get_age(self):
        return self.__age


# -------- Runtime Input --------
name = input("Enter name: ")
age = int(input("Enter age: "))

p = Person(name)
p.set_age(age)

print("Name:", p.name)
print("Age:", p.get_age())'''

'''class Wallet:
    def __init__(self,balance):
        self.__balance = balance

    def add_money(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Added {amount} to wallet.")
        else:
            print("Invalid amount")

    def pay(self,amount):
        if amount>self.__balance:
            print("Not enough balance!..")
        else:
            self.__balance-=amount
            print(f"Paid {amount} successfully.")

    def check_balance(self):
        return self.__balance
    
w = Wallet()
add_amt = int(input())
w.add_money(add_amt)
pay_amt = int(input())
w.pay(pay_amt)
print("Current Wallet Balance =",w.check_balance() )'''


'''class Laptop:
    def __init__(self):
        self.__battery = 50   # default battery

    def set_battery(self, value):
        if 0 <= value <= 100:
            self.__battery = value
            print("Battery updated!")
        else:
            print("Invalid battery value! (0-100 only)")

    def charge(self, value):
        self.__battery += value
        if self.__battery > 100:
            self.__battery = 100
        print(f"Charged by {value}%. Current battery: {self.__battery}%")

    def use(self, value):
        self.__battery -= value
        if self.__battery < 0:
            self.__battery = 0
        print(f"Used {value}%. Current battery: {self.__battery}%")

    def get_battery(self):
        return self.__battery


# ------ Runtime Input ------
l = Laptop()

charge_amt = int(input("Enter charging percent: "))
l.charge(charge_amt)

use_amt = int(input("Enter usage percent: "))
l.use(use_amt)

print("Final Battery Level =", l.get_battery(), "%")'''

'''class Result:
    def __init__(self):
        self.__marks = []   # private list

    def add_mark(self, m):
        if 0 <= m <= 100:
            self.__marks.append(m)
            print("Mark added!")
        else:
            print("Invalid mark!")

    def average(self):
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks) / len(self.__marks)


# -------- Runtime Input --------
r = Result()

n = int(input("How many marks to add? "))

for i in range(n):
    m = int(input("Enter mark: "))
    r.add_mark(m)

print("Average Marks =", r.average())
'''

'''class User:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def set_password(self,new_pwd):
        if len(new_pwd)<6:
            print("Password must have 6 characters!")

        else:
            self.__password = new_pwd
            print("Password updated!")

    def verify(self,pwd):
        if pwd == self.__password:
            return True
        return False
    
username=input()
password=input()
u=User(username,password)
check =input("Enter password to login")
if u.verify(check):
    print("Login Successfull!")
else:
    print("Invelid password..")'''


'''class  Product:
    def __init__(self,name):
        self.name=name 
        self.__price=0
    def set_price(self,price):
        if price>=0:
            self.__price = price
        else:
            print("Invalid price!")
        
    def get_price(self):
        return self.__price
    
    def apply_discount(self,percent):
        discount = (percent/100)*self.__price
        self.__price-=discount

name = input()
price = float(input())
percent = float(input())
obj = Product(name)
obj.set_price(price)
obj.apply_discount(percent)
print("Final Price :",obj.get_price())'''


'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Name: ",self.name)
        print("salary: ",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def show(self):
        super().display()
        print("Department: ",self.department)

name=input()
salary=int(input())
department=input()
obj = Manager(name,salary,department)
obj.show()'''

'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Seats:", self.seats)


# Runtime input
brand = input()
model = input()
seats = int(input())

c = Car(brand, model, seats)
c.show_details()'''


'''class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def work(self):
        print("Manager managing team")

e = Employee()
m = Manager()

e.work()
m.work()'''


'''class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

class SavingsAccount(Bank):
    def __init__(self, bank_name, balance):
        super().__init__(bank_name)
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

class FixedDeposit(SavingsAccount):
    def calculate_interest(self, years):
        return self.balance * 0.07 * years   # 7% interest


fd = FixedDeposit("SBI", 10000)
fd.deposit(2000)
fd.withdraw(3000)
print("Interest for 2 years:", fd.calculate_interest(2))'''

'''from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
class Electriccar(Car):
    def start(self):
        print("Electric car starts silently")

class DieselCar(Car):
    def start(self):
        print("Diesel car starts with engine sound")

obj=Electriccar()
obj1=DieselCar()

obj.start()
obj1.start()'''

'''import math
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return math.pi*math.pow(self.r,2)
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    
r = int(input())
l=int(input())
b=int(input())
v=Shape()
c=Circle(r)
r=Rectangle(l,b)
print(c.area())
print(r.area())'''


'''from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited",amount)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdreawn:",amount)
        else:
            print("Insufficicent funds")

obj = SavingsAccount()
amount = int(input())
obj.deposit(amount)
obj.withdraw(amount)'''


'''from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self,monthlysalary):
        self.monthlysalary = monthlysalary

    def calculate_salary(self):
        return self.monthlysalary
    
class ParttimeEmployee(Employee):
    def __init__(self,hours,rate):
        self.hours=hours
        self.rate=rate

    def calculate_salary(self):
        return self.rate*self.hours
monthlysalary = int(input())
hours=int(input())
rate = int(input())
f=FulltimeEmployee(monthlysalary)
p=ParttimeEmployee(hours,rate)
print(f.calculate_salary())
print(p.calculate_salary())'''

'''from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

    def disconnect(self):
        print("MySQL disconnected")

    def execute_query(self, query):
        print("Executing on MySQL:", query)


class MongoDatabase(Database):
    def connect(self):
        print("Connected to MongoDB")

    def disconnect(self):
        print("MongoDB disconnected")

    def execute_query(self, query):
        print("Executing on MongoDB:", query)


# Testing
m1 = MySQLDatabase()
m1.connect()
m1.execute_query("SELECT * FROM users")
m1.disconnect()

m2 = MongoDatabase()
m2.connect()
m2.execute_query("{ find: 'users' }")
m2.disconnect()'''

'''from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def book_ticket(self, name):
        pass
    
    @abstractmethod
    def cancel_ticket(self, name):
        pass


class BusTransport(Transport):
    def book_ticket(self, name):
        print(name, "Bus ticket booked")

    def cancel_ticket(self, name):
        print(name, "Bus ticket cancelled")


class AirTransport(Transport):
    def book_ticket(self, name):
        print(name, "Flight booked successfully")

    def cancel_ticket(self, name):
        print(name, "Flight cancelled successfully")


b = BusTransport()
b.book_ticket("Vyshu")
b.cancel_ticket("Vyshu")

a = AirTransport()
a.book_ticket("Vyshu")
a.cancel_ticket("Vyshu")'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()'''

'''n=int(input())
for i in range(n,0,-1):
    print("* " * i)'''

'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))'''

'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))'''



