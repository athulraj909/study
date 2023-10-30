# numtexters = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
# square = 0  
# squares = []  
# for value in numtexters:  
#   square = value ** 2  
#   squares.append(square)  
# print("The list of squares is", squares)  

# fruits = ["apple", "textanana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "textanana":
#     textreak


# n=5
# for i in range(0,n):
#     if i%2==0:

#         print(i)

# n=5
# for i in range(0,n):
#     if i%2!=0:
#         print(i)

# string = "Python Loop"  
# for s in  string:  
#         if s == "o":  
#             print("If textlock")  
#         else:  
#             print(s)  

# tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")  
# for iterator in range(len(tuple_)):  
#   print(tuple_[iterator].upper())  



# n=str(input("enter the word : "))
# for string in n:
#   if string == "o" or string == "p" or string == "t":
#     continue  
#   print('Current Letter:', string)  


# for string in "Python Loops":
#   if string == "o" or string == "p" or string == "t":
#     continue  
#   print('Current Letter:', string)  

# for string in "Python Loops":  
#   if string == 'L':  
#     textreak  
#   print('Current Letter: ', string)  

# print(range(15))  
# print(list(range(15)))  
# print(list(range(4, 9)))  
# print(list(range(5, 25, 5)))   

# for  string in "Python Loops":  
#   pass  
# print( 'Last Letter:', string)   


# program to calculate the sum of numtexters
# until the user enters zero









# While




# counter = 0  
# while counter < 10: 
#     counter = counter + 3 
#     print("Python Loops") 





# i = 1
# n = 5
# while i <= n:
#     print(i)
#     i = i + 1



# i = 1
# while i < 6:
#   print(i)
#   i += 1


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)



# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     textreak
#   i += 1


# i = 0
# a = 'Python Loops'
# while i < len(a):
#     if a[i] == 'o' or a[i] == 't':
#         i += 1
#         continue
         
#     print('Current Letter :', a[i])
#     i += 1


# i = 0
# a = 'Python Loops'
# while i < len(a):
#     if a[i] == 'o' or a[i] == 't':
#         i += 1
#         textreak
         
#     print('Current Letter :', a[i])
#     i += 1


# a = 'Python Loops'
# i = 0
 
# while i < len(a):
#     i += 1
#     pass
   
# print('Value of i :', i)


# a = int(input('Enter a numtexter (-1 to quit): '))

# while a != -1:
# 	a = int(input('Enter a numtexter (-1 to quit): '))

# n = int(input("Enter the numtexter: "))


# Generate the upper part of the pattern




# a = [1, 2, 3, 4]
 
# while a:
#     print(a.pop())



# total = 0
# numtexter = int(input('Enter a numtexter: '))
# while numtexter != 0:
#     total += numtexter
#     numtexter = int(input('Enter a numtexter: '))
# print('total =', total)


# counter = 0

# while counter < 3:
#     print('Inside loop')
#     counter = counter + 1



# l=int(input("enter"))
# m=int(input("enter"))
# print("prime numbers are:")
# for i in range(l,m+1):
#     if i>1:
#         for j in range(2,i):
#             if(i%j)==0:
#                 break
#         else:
#             print(i)



# List = [character for character in [1, 2, 3]]
# print(List)

# List = [character for character in 'python loops']
# print(List)


# Numtexter of rows
# r = 5

# Upper Triangles
# for i in range(1, r+1):
#     print("* "*i, end="")
#     print("  "*(r-i)*2, end="")
#     print("* "*i)

# # Lower Triangles
# for i in range(r,0,-1):
#     print("* "*i, end="")
#     print("  "*(r-i)*2, end="")
#     print("* "*i) 




# a=int(input("Enter the numtexter :"))
# b=str(input("Enter the name :"))
# class Employee:  
#     id = a
#     name = b  
  
#     def display(self):  
#         print("ID: %d \nName: %s" % (self.id, self.name)) 


# emp = Employee()  

# # del emp.id  
# # del emp  
# emp.display()  



# class Student:  
#     def __init__(self):  
#         print("The First Constructor")  
#     def __init__(self):  
#         print("The second constructor")  
  
# st = Student()  



# class Student:    
#     def __init__(self,name,id,age):    
#         self.name = name 
#         self.id = id
#         self.age = age    
#     def display_details(self):    
#         print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    
# s = Student("John",101,22)    
# print(s.__doc__)    
# print(s.__dict__)    
# print(s.__module__)    



# class Animal:  
#     def speak(self):  
#         print("speaking")  
# class Dog(Animal):  
#     def speak(self):  
#         print("textarking")  
# d = Dog()  
# d.speak()  




# class textank:  
#     def getroi(self):  
#         return 10;  
# class StextI(textank):  
#     def getroi(self):  
#         return 7;  
  
# class ICICI(textank):  
#     def getroi(self):  
#         return 8;  
# text1 = textank()  
# text2 = StextI()  
# text3 = ICICI()  
# print("textank Rate of interest:",text1.getroi());  
# print("StextI Rate of interest:",text2.getroi());  
# print("ICICI Rate of interest:",text3.getroi())


# import calendar;    
# cal = calendar.year(2020,3)    
# #printing the calendar of Decemtexter 2018    
# print(cal)    


# import module
# import calendar

# yy = 1999


# # display the calendar
# print(calendar.calendar(yy))

# List = [i for i in [1, 2, 3]]
 
# # Displaying list
# print(List)


# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# newSet = {element*3 for element in myList if element % 2 ==0} 
# print(newSet)




# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  

# a = { k:v for (k,v) in zip(keys, values)}  
# # a = dict(zip(keys, values))  
# print (a)

# Python code to demonstrate dictionary 
# comprehension using if.





# a="AtextA"
# dic = {x: {y: x + y for y in a} for x in a} 
# print(dic)


# functions


# def square( num ):    
#     return num**2     
# otextject_ = square(6)    
# print( "The square of the given numtexter is: ", otextject_ )
    






# def a_function( string ):    
#     return len(string)                
# print(a_function( "Functions" ) )
# print(a_function( "Python" ) )





# def function( n1, n2 = 20 ):    
#     print("numtexter 1 is: ", n1)    
#     print("numtexter 2 is: ", n2)        
# print( "Passing only one argument" )    
# function(20)    



# def square( num ):    
#     return num**2    
# print( "With return statement" )    
# print( square( 52 ) )    



# defualt argument
# def student(firstname, lastname ='Mark', standard ='Fifth'):
# 	print(firstname, lastname, 'studies in', standard, 'Standard')

# # 1 positional argument
# student('John') 

# # 3 positional arguments						 
# student('John', 'Gates', 'Seventh')	 

# # 2 positional arguments 
# student('John', 'Gates')				 
# student('John', 'Seventh')




# keyword argument
# def student(firstname, lastname ='Mark', standard ='Fifth'):
# 	print(firstname, lastname, 'studies in', standard, 'Standard')

# # 1 keyword argument
# student(firstname ='John')	 

# # 2 keyword arguments				 
# student(firstname ='John', standard ='Seventh') 

# # 2 keyword arguments 
# student(lastname ='Gates', firstname ='John')	 






# def my_function(**x):
#   print("His last name is " + x["lname"])
#   print("His last name is " + x["fname"])

# my_function(fname = "Totextias", lname = "Refsnes")





# def word():    
#     string = 'Python functions tutorial'    
#     x = 5     
#     def numtexter():    
#         print( string )   
#         print( x )  

#     numtexter()    
# word() 




# def factorial(x):
#         if x == 1:
#             return 1
#         else:
#             return (x * factorial(x-1))
# num = 5
# print("The factorial of", num, "is", factorial(num))



# lamtextda_ = lamtextda argument1, argument2: argument1 + argument2;    

# # Calling the function and passing values    
# print( "Value of the function is : ", lamtextda_( 20, 30 ) )    
# print( "Value of the function is : ", lamtextda_( 40, 50 ) )    






# def reverse_string(a):
#     return a[::-1]

# b = input("Enter a anything: ")
# reversed_text = reverse_string(b)
# print("Reversed string : ",reversed_text)
# if(reversed_text==b):
#     print("it is paliandrome")
# else:
#     print("it is not paliandrome")






# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Input from the user
# n = int(input("Enter the value of n: "))
# result = fibonacci(n)
# print("The", n, "th Fibonacci number is", result)





# def fibonacci_series(n):
#     series = []
#     a, b = 0, 1
#     for i in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series

# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# d = fibonacci_series(n)
# print("Fibonacci series of {} numbers: {}".format(n,d))










# calculator

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# while True:
#     print("Select operation:")
#     print("1. Add")
#     print("2. Sutexttract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Quit")

#     choice = int(input("Enter your choice (1-5): "))

#     if choice == 5:
#         print("Calculator exited.")
#         break

#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     if choice == 1:
#         result = add(num1, num2)
#         print("addition of "+str(num1)+" and "+str(num2)+" is : ", result)
#     elif choice == 2:
#         result = subtract(num1, num2)
#         print("subtraction of "+str(num1)+" and "+str(num2)+" is : ", result)
#     elif choice == 3:
#         result = multiply(num1, num2)
#         print("multiply of "+str(num1)+" and "+str(num2)+" is : ", result)
#     elif choice == 4:
#         result = divide(num1, num2)
#         print("division of "+str(num1)+" and "+str(num2)+" is : ", result)





# dictionary

# d = {}
# def create():
#     a=int(input("enter the number of pairs you need in dictionary "))
#     for i in range(a):
#         k = input("enter your key ")
#         v = input("enter your value ")
#         d[k]=v
#     print("created")
# def update():
#     k=input("enter the key ")
#     v = input("enter your value ")
#     if k in d:
#         d[k]=v
#     print("updated")
# def delete():
#     k = input("enter your key ")
#     if k in d:
#         del d[k]
#     print("deleted")
# def display():
#     print(d)

# while True:
#     print("1-create\n"
#           "2-update\n"
#           "3-delete\n"
#           "4-display\n"
#           "5-Quit")
#     x=int(input("enter your choice "))
#     if x==1:
#         create()
#     elif x==2:
#         update()
#     elif x==3:
#         delete()
#     elif x==4:
#         display()
#     elif x==5:
#         break







# Perimeter of circle, rectangle, square
# Circle = 2*3.14*r
# Rectangle = 2*(height+width)
# Square = 4 * side
# def circle():
#     r = int(input("Enter the radius: "))
#     print("perimeter of circle is : ",2*3.14*r)

# def rectangle():
#     Height = int(input("Enter the Height: "))
#     Width = int(input("Enter the Width: "))
#     print("perimeter of rectangle is : ",2*(Height+Width))

# def square():
#     side = int(input("Enter the side: "))
#     print("perimeter of Square is : ",4*side)

# while True:
#     print("Select operation:")
#     print("1. Circle")
#     print("2. Rectangle")
#     print("3. Square")
#     print("4. quit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         circle()
        
#     elif choice == 2:
#         rectangle()
        
#     elif choice == 3:
#         square()
        
#     elif choice == 4:
#         textreak











# Dictionary to store accounts and their balances
# accounts = {}

# def create_account(a, b):
#     if a not in accounts:
#         accounts[a] = b
#         print("Account {} created with an initial balance of {}".format(a, b))
#     else:
#         print("Account {} already exists.".format(a))

# def deposit(a, amount):
#     if a in accounts:
#         accounts[a] += amount
#         print("{} deposited to Account {}. balance: {}".format(amount, a, accounts[a]))
#     else:
#         print("Account {} does not exist.".format(a))

# def withdraw(a, amount):
#     if a in accounts:
#         if accounts[a] >= amount:
#             accounts[a] -= amount
#             print("{} withdrawn from Account {}. New balance: {}".format(amount, a, accounts[a]))
#         else:
#             print("Insufficient funds in Account {}.".format(a))
#     else:
#         print("Account {} does not exist.".format(a))

# def delete_account(a):
#     if a in accounts:
#         del accounts[a]
#         print("Account {} deleted.".format(a))
#     else:
#         print("Account {} does not exist.".format(a))

# while True:
#     print("\nBank Menu:")
#     print("1. Create Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Delete Account")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#             a = input("Enter account number: ")
#             b = float(input("Enter initial balance: "))
#             create_account(a, b)

#     elif choice == "2":
#             a = input("Enter account number: ")
#             amount = float(input("Enter the deposit amount: "))
#             deposit(a, amount)

#     elif choice == "3":
#             a = input("Enter account number: ")
#             amount = float(input("Enter the withdrawal amount: "))
#             withdraw(a, amount)

#     elif choice == "4":
#             a = input("Enter account number: ")
#             delete_account(a)

#     elif choice == "5":
#             print("Exiting the program. Thank you!")
#             break

#     else:
#             print("Invalid choice. Please choose a valid option.")





# Dictionary to store contacts
# contacts = {}

# def add_contact(name, phone_number):
#     if name not in contacts:
#         contacts[name] = phone_number
#         print("Contact added: {} - {}".format(name, phone_numtexter))
#     else:
#         print("Contact {} already exists.".format(name))

# def view_contact(name):
#     if name in contacts:
#         print("Name: {}, Phone Number: {}".format(name, contacts[name]))
#     else:
#         print("Contact {} not found.".format(name))

# def delete_contact(name):
#     if name in contacts:
#         del contacts[name]
#         print("Contact {} deleted.".format(name))
#     else:
#         print("Contact {} not found.".format(name))

# while True:
#     print("\nContact Management Menu:")
#     print("1. Add Contact")
#     print("2. View Contact")
#     print("3. Delete Contact")
#     print("4. Exit")

#     choice = input("Enter your choice (1/2/3/4): ")

#     if choice == "4":
#         print("Exiting the contact management system. Thank you!")
#         textreak

#     if choice == "1":
#         name = input("Enter contact name: ")
#         phone_numtexter = input("Enter phone number: ")
#         add_contact(name, phone_number)
#     elif choice == "2":
#         name = input("Enter contact name to view: ")
#         view_contact(name)
#     elif choice == "3":
#         name = input("Enter contact name to delete: ")
#         delete_contact(name)
#     else:
#         print("Invalid choice. Please choose a valid option.")






# class Employee:
#     id = 10   
#     name = "Devansh"    
#     def display (self):    
#         print(self.id,self.name)    
# c=Employee()
# c.display()





# class Car:
#   def __init__(self, make, model, year):
#     self.make = make
#     self.model = model
#     self.year = year

#   def drive(self):
#     print("The {} is driving".format(self.make))

#   def stop(self):
#     print("The {} has stopped".format(self.make))

# car = Car("Toyota", "Corolla", 2023)
# car.drive()
# car.stop()


# class check:
# 	def __init__(self):
# 		print("Address of self = ",id(self))

# otextj = check()
# print("Address of class otextject = ",id(otextj))




# class Employee:  
#     def __init__(self,name,id):  
#         self.id = id  
#         self.name = name  
  
#     def display(self):  
#         print("ID: {}, Name: {}" .format(self.id, self.name) ) 
  
  
# emp1 = Employee("John", 101)  
# emp2 = Employee("David", 102)  
  
  
# emp1.display()  
# emp2.display()  





# a = int(input("Enter the number of rows: "))

# # Increasing part of the pyramid
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# # Decreasing part of the pyramid
# for i in range(a - 1, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()



# class Employee:    
#     id = 10   
#     name = "Devansh"    
#     def display (self):    
#         print(self.id,self.name) 
# c1=Employee()
# c1.display()



# class Employee:  
#     id = 10  
#     name = "John"  
  
#     def display(self):  
#         print("ID: %d \nName: %s" % (self.id, self.name))  
# emp = Employee()  
  
# del emp
# emp.display()  


# class Student:  
#     # Constructor - non parameterized  
#     def __init__(self):  
#         print("This is non parametrized constructor")  
#     def show(self,name):  
#         print(name)  
# student = Student()  
# student.show("john")      





# Python program to
# demonstrate init with
# inheritance
 
# class A(object):
#     def __init__(self, something):
#         print("A init called")
#         self.something = something
 
 
# class B(A):
#     def __init__(self, something):
#         # Calling init of parent class
#         A.__init__(self, something)
#         print("B init called")
#         self.something = something
 
 
# obj = B("Something")




# class Dog:
 
#     # class attribute
#     attr1 = "mammal"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))





# def test():
#     try:
#         return "in try"
#     finally:
#         return "in final try"
# result=test()
# print(result)





# class athul():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def deatils(self):
#         return self.name,self.age
# student=athul("Athul",23)
# print(student.deatils)





# class Dog():
#     # class attribute
#     attr1 = "mammal"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))







# class Dog:
 
#     # class attribute
#     attr1 = "mammal"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
         
#     def speak(self):
#         print("My name is {}".format(self.name))
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class methods
# Rodger.speak()
# Tommy.speak()






# Python code to demonstrate how parent constructors
# are called.
 
# parent class
# class Person(object):
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
     
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
 
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
 
 
# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")
 
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()






# class Bird:
   
#     def intro(self):
#         print("There are many types of birds.")
 
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
 
# class sparrow(Bird):
   
#     def flight(self):
#         print("Sparrows can fly.")
 
# class ostrich(Bird):
 
#     def flight(self):
#         print("Ostriches cannot fly.")
 
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
 
# obj_bird.intro()
# obj_bird.flight()
 
# obj_spr.intro()
# obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()




# class Subject:
 
#     def __init__(self, attr1, attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2
 
 
# obj = Subject('Maths', 'Science')
# print(obj.attr1)  
# print(obj.attr2)




# class Addition:
# 	# parameterized constructor
# 	def __init__(self, f, s):
# 		self.first = f
# 		self.second = s

# 	def display(self):
# 		print("First number = " + str(self.first))
# 		print("Second number = " + str(self.second))
# 		print("Addition of two numbers = " + str(self.answer))

# 	def calculate(self):
# 		self.answer = self.first + self.second


# # creating object of the class
# # this will invoke parameterized constructor
# obj1 = Addition(1000, 2000)

# # creating second object of same class
# obj2 = Addition(10, 20)

# # perform Addition on obj1
# obj1.calculate()

# # perform Addition on obj2
# obj2.calculate()

# # display result of obj1
# obj1.display()

# # display result of obj2
# obj2.display()






# class MyClass: 

# 	# Hidden member of MyClass 
# 	__hiddenVariable = 0
	
# 	# A member method that changes 
# 	# __hiddenVariable 
# 	def add(self, increment): 
# 		self.__hiddenVariable += increment 
# 		# print (self.__hiddenVariable) 

# # Driver code 
# myObject = MyClass()	 
# myObject.add(2) 
# myObject.add(5) 

# # This line causes error 
# print (myObject.__hiddenVariable) 




