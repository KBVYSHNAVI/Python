#Resversing a number:
'''n=int(input())                                                                      #abs -->is the function which convert -ve to +ve
answer=0                                                                               #is.alpha()-->it is used to check whether the variable s alphabet or not
while n>0:
    last=n%10                                                                          #ord-->it  is used to know the ascii value from alphabet to number
    answer=answer*10+last
    n//=10                                                                             #chr-->it is used to check ascii value from number to alphabet
print(answer)'''


'''#Palindrome number
n=int(input())
o=n    # o means original number
r = 0  # r means reverse
while n>0:
     digit = n % 10
     r= r * 10 + digit
     n = n // 10
if o == r:
    print("It's a palindrome!")
else:
    print("Not a palindrome!!.")'''

#palindrome numbers between 1-1000
'''for i in range(1,1001):
    a=i
    ans=0
    while i>0:
        last=i%10
        ans=ans*10+last
        i//=10
    if ans==a:
        print(a)'''

# palindrome in words
'''''
word = input("Enter a word: ").lower()    #--->here   .lower() it is used for case insensitive

if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
    '''
#printing prime numbers:
'''n=int(input())
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
        print(i)'''


#Sum of numbers until single digit
'''n=int(input())
ans=0
while n>9:
    while n>0:
        last=n%10
        ans+=last
        n//=10
    n=ans
    ans=0
print(n)'''

#reversing an integer with -ve values
'''''
class Solution(object):
    def reverse(self, x):
        mini=-2**31
        maxi=2**31-1
        sign=-1 if x<0 else 1
        answer=0
        x=abs(x)
        while x!=0:
            last=x%10
            answer=answer*10+last
            x//=10
        answer*=sign
        if answer<mini or answer>maxi:
            return 0
        return answer'''

    
    # pattern of hollow square
'''''
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''



 
# trapezium patterns
'''''
n=4
a=1
b=n*n+1
for i in range(n,0,-1):
    for h in range(0,n-i):
        print("--",end=' ')
    for j in range(i):
        print(f"{a}*",end='')
        a+=1
    for k in range(i-1):
        print(f"{b}*",end='')
        b+=1
    print(b)
    b=b-2*(i-1)'''

#kaperkar number
'''''
n=int(input())
sq=n**2
t=n
count=0
while n>0:
    n//=10
    count+=1
p=10**count
rem=sq%p
q=sq//p
ans=rem+q
if ans==t:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")'''

#Multiplication of a table
'''''
num=int(input())
for i in range(1,11):
    print(f"{num}*{i}={num*i}")'''

#counting a vowels in a sentence
'''''
sen=input()
vow='aeiouAEIOU'
count=0
for char in sen:
    if char in vow:
        count+=1
print (count)'''
                                                                              
#from alphabet to ascii
'''print(ord(input()))'''
#from number to alphabet
'''print(chr(int(input())))'''


#List--->Immutable
#Sorting elements desending order
'''''
l=[1,2,100,98,78,69,96]
l.sort(reverse=True)
print(l)'''

#elements in ascending order
'''''
l=[1,2,100,98,78,69,96]
l.sort()
print(l)'''
'''
l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
    for i in l:
        print(i)   '''


# giving outputs without duplicate numbers

'''l=list(map(int,input().split()))
ans=[]
for i in l:
    if i not in ans:
        ans.append(i)
#[print(x) for x in ans]--> for printing output in vertical line
[print(x,end=' ') for x in ans] ''' #--> for printing  output in horizontal line '''

#set ---> It is denoted by curly brackets and it is immutable                           ---->it not allow duplicate elements
#sorted is a function used in set and tuple                                             ---->we can convert any data type into list datatype by using list()
#'*'-->unpacking of variable we use this                                                --->set and dictionary both have same data types
#CRUD OPERATIONS    -->creating,reading,uppdation,deletion.
'''
#checking lists same or not
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
k = sum(l1)
m = sum(l2)
if l1 == l2 and k == m:
    print("Same")
else:
    print("Not same")'''


'''
#removing duplicate elements
l=list(map(int,input().split()))
ans=[]
for i in l:
    if i not in ans:
        ans.append(i)
[print(x,end=" ") for x in ans ]'''

#giving the output as length of the list
'''
s=[1,2,3,4,5,6]
dup=set(s)
print(len(dup))'''
#to know whether the the number is compatible or in compatible
'''
n1=int(input())
n2=int(input())
l1=list(map(int,input().split()))  
l2=list(map(int,input().split()))
if n1 != n2:
    print("Incompatible")
else:
    for i in range(n1):
        if l1[i] < l2[i]:
            print("Incompatible")
            break
        else:
        print("Compatible")'''

#sum of even and odd in a list
'''
n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for num in l:
    if num%2==0:
        es+=num
    else:
        os+=num
print(f"The sum of even numbers in the list is {es}")
print(f"The sum of odd numbers in the list is {os}")'''

#creating 2 dimensional list
'''rows, cols = map(int, input().split())
ll = []
for i in range(rows):
    row = list(map(int, input().split()))
    ll.append(row)
for i in range(rows):
    for j in range(cols):
        print(ll[i][j],end=" ")                      #-->here  in both above 2 lists output is same but approach is different
    print()'''

#same creation by using list comprehension
'''rows,cols=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(lst[i][j],end=" ")
    print()'''

#string: a group of characters and immutable
#finding factorialby using function
'''def findfact(n):
    power=1
    for i in range(1,n+1):
        power*=i
    return power
a=7
b=9
c=4
print(findfact(a))
print(findfact(b))
print(findfact(c))'''

#a function with zero parameters and without return type
'''def sayHi():
    print("Hi")
sayHi()'''

#a function with parameter without returning a value
'''def sayHi(name):
    print("Hi!",name)
name="vyshnaviveeresh"
sayHi(name)'''

'''def sayHi(name="Guest"):
    print("Hi!",name)
sayHi()'''

'''def sayHi(s='vyshnavi'):
    print(s)
sayHi()
sayHi("Harshitha")'''

#without parameer with return type
'''''
def sayHi():
    return "vyshnavi"
print(sayHi())
name=sayHi()
print(name)'''


'''''
def findsquare(x):
    return x*x
def findsumofsquares(x,y):
    return findsquare(x)+findsquare(y)
print(findsquare(10))
print(findsumofsquares(3,4))'''

#RECURSION:A FUNCTION CALL ITSELF CALLED RECURSION
'''n = 5
def printN(n):
    if n == 0:
        return
    printN(n - 1)
    print(n,end = " ")
printN(n)
print('Completed Vyshnavi!!!')'''

#finding factorial
'''n=10
def findfact(n):
    if n==1 or n==0:
        return 1
    return n*findfact(n-1)
print(findfact(n))'''


#alternate to switch case in python
'''def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))'''

'''''
import string
print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)
print("All digits:", string.digits)
print("All punctuation:", string.punctuation)'''

#generating random password
'''import string
import random
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(10))
print("Random password:", password)'''

#fibonacci series
'''n=int(input())
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(n))'''

#printing the numbers in list vertically
'''my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
   print(my_list[index])
   index += 1'''

#knowing the length
'''lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])'''

#list comprehension
'''numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers)'''

#printing random numbersanad creating list
'''import random
l1=[]
for i in range(5):
    x=random.randint(0,100)
    l1.append(x)
print(l1)'''

#unpacking of variables
'''tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)'''

#printing fibonacci series by using loops 
'''n=int(input())
def findfibo(n):
    f=0 #f=first s=second
    s=1
    cal=0
    print(f,s)
    lst=[0,1]
    for i in range(n):
        cal=f+s
        lst.append(cal)
        print(cal)
        f=s
        s=cal
    return lst[n]
lst=findfibo(n)
print(lst)'''

#finding gcd by using recursion
'''a,b=map(int,input().split())
def gcd(a,b):
  if b<=0:
    return a
  return gcd(b,a%b)
print(gcd(a,b))'''

#finding gcd using loops
'''n,m=map(int,input().split())
def findgcd(n,m):
    gcd=1
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            gcd=i
    return gcd
print(findgcd(n,m))'''

#perfect number-->sum of divisors
'''n=int(input())
divisors=[]
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)
print(divisors)'''

#oops concepts
'''class Venue:
    def __init__(self,name,city):
        self.Vname=name
        self.Vcity=city

    def display(self):
        print("Venue details")
        print("Venue name :"+self.Vname)
        print("City name: "+self.Vcity)
print("Enter the venue details:")
user_input=input().strip()
details=user_input.split(",")
Vname=details[0].strip()
Vcity=details[1].strip()


v=Venue(Vname,Vcity)
v.display()
'''

'''l1 = [10,20,30,40]
l2 = [10,20,30]
joined = []
for i in range(len(l2)):   # smallest list length
    joined.append(l1[i] * l2[i])

print(joined)
'''

'''l1 = [[1,2],[3,4]]
l2 = [[5,6],[7,8]]

result = []
for i in range(len(l1)):
    row = []
    for j in range(len(l1[0])):
        row.append(l1[i][j] * l2[i][j])
    result.append(row)

print(result)'''


'''class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

name = input()
age = int(input())
marks=int(input())
s1 = Student(name,age,marks)
s1.display()'''

'''import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        pi = 3.14
        area = pi*math.pow(self.r,2)
        return area

    def perimeter(self):
        pi = 3.14
        perimeter = 2*pi*self.r
        return perimeter

r=int(input())
v = Circle(r)
print(v.area())
print(v.perimeter())'''

'''class BankAccount:
    def __init__(self,accno,balance):
        self.accno = accno
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        print("Deposited: ",amount)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdraw: ",amount)

    def show(self):
        print("accno",self.accno)
        print("Current Balance:",self.balance)

accno = int(input())
balance = int(input())
v2=BankAccount(accno,balance)
amount = int(input())
v2.deposit(amount)
v2.show()'''

'''class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
a=int(input())
b = int(input())
obj = Calculator(a,b)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())'''

'''class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area = self.l*self.b
        return area

    def perimeter(self):
        perimeter = 2*(self.l+self.b)
        return perimeter

    def is_square(self):
        return self.l == self.b
    
l = int(input())
b=int(input())
obj = Rectangle(l,b)
print(obj.area())
print(obj.perimeter())
if obj.is_square():
    print("It is Square...")
else:
    print("It is not square....")'''

'''class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting....")

    def stop(self):
        print("Car is stopping...")

    def display(self):
        print("Brand: ",self.brand)
        print("Model:",self.model)
        print("Year: ",self.year)

brand = input()
model = input()
year = input()
obj = Car(brand,model,year)
obj.start()
obj.stop()
obj.display()'''

'''class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author=author
        self.available =available

    def borrow(self):
        if self.available:
            self.available = False
            print("You borrowed the book..")
        else:
            print("Book is not available..")

    def return_book(self):
        self.available = True
        print("Book returned successfully..")

title = input()
author = input()
obj = Book(title,author)
obj.borrow()
obj.return_book()'''


'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        if len(self.marks)==0:
            return 0
        else:
            return sum(self.marks)/len(self.marks)
        
name = input()
n = int(input())
marks = []
for i in range(n):
    marks.append(int(input()))
obj = Student(name,marks)
print(obj.average())'''

'''class Product:
    def __init__(self,proname,price,quantity):
        self.proname = proname
        self.price = price
        self.quantity= quantity

    def totalprice(self):
        return self.price*self.quantity
    
proname = input()
price = int(input())
quantity = float(input())

obj = Product(proname,price,quantity)
print(obj.totalprice())
'''

'''class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)
        print(item.name,"added from the cart")

    def remove_item(self,item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)
                print(item_name,"removed from cart.")
                return 
        print(item_name,"not found in the cart.")

    def total_amount(self):
        total=0
        for i in self.items:
            total+=i.price
        return total
    
obj = Cart()
while True:
    print("\n1.Add item")
    print("2.Remove item")
    print("3.Total amount")
    print("4.Exit")

    choice = int(input())
    if choice == 1:
        name = input()
        price=float(input())
        item = Item(name,price)
        obj.add_item(item)

    elif choice == 2:
        name = input()
        obj.remove_item(name)

    elif choice == 3:
        print(obj.total_amount())

    elif choice==4:
        break
    else:
        print("Invaled Choice")'''

'''class Course:
    def __init__(self,coursename):
        self.coursename = coursename

class Student:
    def __init__(self,name):
        self.name=name
        self.courses=[]
    def enroll_course(self,course):
        self.courses.append(course)
        print(f"{self.name} enrolled in  {course.coursename}")

    def display(self):
        print(f"Courses of {self.name}:")
        for c in self.courses:
            print("-",c.coursename)

name = input()
s = Student(name)
n=int(input("How many courses enrolled:"))
for i in range(n):
    cname = input(f"Enter course{i+1} name: ")
    c=Course(cname)
    s.enroll_course(c)
s.display()'''





    

    

