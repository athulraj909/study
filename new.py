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
  
# del emp.id  
# del emp  
# emp.display()  




# class Student:  
#     def __init__(self):  
#         print("The First Constructor")  
#     def __init__(self):  
#         print("The second constructor")  
  
# st = Student() 





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







# # parent class
# class Person():

# 	# __init__ is known as the constructor
# 	def __init__(self, name, idnumber):
# 		self.name = name
# 		self.idnumber = idnumber

# 	def display(self):
# 		print(self.name)
# 		print(self.idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("IdNumber: {}".format(self.idnumber))
	
# # child class
# class Employee(Person):
# 	def __init__(self, name, idnumber, salary, post):
# 		self.salary = salary
# 		self.post = post

# 		# invoking the __init__ of the parent class
# 		Person.__init__(self, name, idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("IdNumber: {}".format(self.idnumber))
# 		print("Post: {}".format(self.post))


# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")

# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()






# class Question:
#     def __init__(self, question_text, correct_answer):
#         self.question_text = question_text
#         self.correct_answer = correct_answer

#     def ask_question(self):
#         print(self.question_text)

#     def check_answer(self, user_answer):
#         return user_answer == self.correct_answer

# # Create instances of the Question class
# question1 = Question("What is the capital of France?", "Paris")
# question2 = Question("What is 2 + 2?", "4")
# question3 = Question("What is the largest planet in our solar system?", "Jupiter")

# # Ask questions and check answers
# questions = [question1, question2, question3]

# for question in questions:
#     question.ask_question()
#     user_answer = input("Your answer: ")
    
#     if question.check_answer(user_answer):
#         print("Correct!\n")
#     else:
#         print("Wrong! The correct answer is {}\n".format(question.correct_answer))




# class Bird:

# 	def intro(self):
# 		print("There are many types of birds.")

# 	def flight(self):
# 		print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):

# 	def flight(self):
# 		print("Sparrows can fly.")

# class ostrich(Bird):

# 	def flight(self):
# 		print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()






# # A simple Python function to demonstrate 
# # Polymorphism

# def add(x, y, z = 0): 
# 	return x+y+z

# # Driver code 
# print(add(2, 3))
# print(add(2, 3, 4))








# class India():
# 	def capital(self):
# 		print("New Delhi is the capital of India.")
# 	def language(self):
# 		print("Hindi is the most widely spoken language of India.")
# 	def type(self):
# 		print("India is a developing country.")
# class USA():
# 	def capital(self):
# 		print("Washington, D.C. is the capital of USA.")
# 	def language(self):
# 		print("English is the primary language of USA.")
# 	def type(self):
# 		print("USA is a developed country.")
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
# 	country.capital()
# 	country.language()
# 	country.type()






# # Python program to 
# # demonstrate protected members 

# # Creating a base class 
# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 
# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
		
# obj1 = Base()
# obj2 = Derived()
# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 
# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 







# # Python program to 
# # demonstrate private members 

# # Creating a Base class 
# class Base: 
# 	def __init__(self): 
# 		self.a = "hello"
# 		self.__c = "world"
# 		# print(self.__c)

# class Derived(Base): 
# 	def __init__(self): 

# 		Base.__init__(self) 
# 		print("Calling private member of base class: ") 
# 		print(self.__c) 

# # Driver code 
# obj1 = Base() 
# print(obj1._Base__c)
# # print(obj1.a) 
# # obj2=Derived()
# # Uncommenting print(obj1.c) will 
# # raise an AttributeError 

# # Uncommenting obj2 = Derived() will 
# # also raise an AttributeError as 
# # private member of base class 
# # is called inside derived class 






# class MyClass: 

# 	# Hidden member of MyClass 
# 	__hiddenVariable = 0
	
# 	# A member method that changes 
# 	# __hiddenVariable 
# 	def add(self, increment): 
# 		self.__hiddenVariable += increment 
# 		print (self.__hiddenVariable) 

# # Driver code 
# myObject = MyClass()	 
# myObject.add(2) 
# myObject.add(5) 

# # This line causes error 
# print(myObject._MyClass__hiddenVariable)






# # A Python program to demonstrate that hidden 
# # members can be accessed outside a class 
# class MyClass: 

# 	# Hidden member of MyClass 
# 	__hiddenVariable = 10

# # Driver code 
# myObject = MyClass()	 
# print(myObject._MyClass__hiddenVariable) 





# class Test: 
# 	def __init__(self, a, b): 
# 		self.a = a 
# 		self.b = b 

# 	def __repr__(self): 
# 		return "Test a:%s b:%s" % (self.a, self.b) 

# 	def __str__(self): 
# 		return "From str method of Test: a is %s,b is %s" % (self.a, self.b) 

# # Driver Code		 
# t = Test(1234, 5678) 
# print(t) # This calls __str__()
# print([t]) # This calls __repr__() 




# # Python program to 
# # demonstrate private members 

# # Creating a Base class 
# class Base: 
# 	def __init__(self): 
# 		self.a = "hello"
# 		self.__c = "world"
# 		print(self.__c)

# class Derived(Base): 
# 	def __init__(self): 

# 		Base.__init__(self) 
# 		print("Calling private member of base class: ") 
# 		print(self.__c) 

# # # Driver code 
# obj1 = Base() 
# print(obj1.__c)
# print(obj1.a) 
# obj2=Derived()
# print(obj2.__c)
# # Uncommenting print(obj1.c) will 
# # raise an AttributeError 

# # Uncommenting obj2 = Derived() will 
# # also raise an AttributeError as 
# # private member of base class 
# # is called inside derived class 






# class Account():
#     def __init__(self, account_number, account_balance):
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def withdraw(self, amount):
#         if self.account_balance - amount > 0:
#             self.account_balance = self.account_balance - amount
#         else:
#             print("insufficient balace  ")

#     def deposit(self,depo):
#         if self.account_balance + depo > 0:
#             self.account_balance = self.account_balance + depo
        
#     def display(self):
#         print("Your account balance is {}".format(self.account_balance))

# # a=input("Enter account number : ")
# # b=input("enter the initial amount : ")

# account_one = Account('1234',5000)
# account_two = Account('234',2000)
# account_one.withdraw(100)
# account_two.withdraw(100)
# # account_one.deposit(200)
# account_one.display()
# account_two.display()







# class Account:
#     def __init__(self, account_number, account_balance):
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def withdraw(self, amount):
#         if self.account_balance - amount >= 0:
#             self.account_balance -= amount
#             print("Your Account Balance is : ",self.account_balance)
#         else:
#             print("Insufficient balance")

#     def deposit(self, depo):
#         if depo > 0:
#             self.account_balance += depo
#             print("Your Account Balance is : ",self.account_balance)

#     def display(self):
#         print("Account Number: {}".format(self.account_number))
#         print("Account Balance: {}".format(self.account_balance))

# account_number = input("Enter account number: ")
# initial_balance = float(input("Enter the initial balance: "))

# user_account = Account(account_number, initial_balance)

# while True:
#     print("\nChoose an action:")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Display Account Info")
#     print("4. Exit")

#     choice = input("Enter your choice (1/2/3/4): ")

#     if choice == '1':
#         amount = float(input("Enter the amount to withdraw: "))
#         user_account.withdraw(amount)
#     elif choice == '2':
#         deposit_amount = float(input("Enter the amount to deposit: "))
#         user_account.deposit(deposit_amount)
#     elif choice == '3':
#         user_account.display()
#     elif choice == '4':
#         break
#     else:
#         print("Invalid choice. Please choose a valid option.")







# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.physics = 0
#         self.chemistry = 0
#         self.maths = 0

#     def enter_marks(self):
#         self.physics = float(input("Enter Physics marks: "))
#         self.chemistry = float(input("Enter Chemistry marks: "))
#         self.maths = float(input("Enter Maths marks: "))
    
#     def find_total(self):
#         self.total = self.physics + self.chemistry + self.maths
#         print("Total marks for student {} (ID: {}) is: {}".format(self.name, self.id, self.total))


# name = input("Enter student name: ")
# id = int(input("Enter student ID: "))

# student = Student(name, id)

# student.enter_marks()

# student.find_total()






# class Customer:
#     def __init__(self,customer_id, quantity, price):
#         self.customer_id = customer_id
#         self.quantity = quantity
#         self.price = price
#         self.discount = 0
    
#     def generate_bill(self):
#         price = self.quantity * self.price
#         self.discount_amount = price * self.discount
#         return price - self.discount_amount
    
# class SilverCustomer(Customer):
#     def __init__(self,id, quantity, price):
#         Customer.__init__(self,id,quantity,price)
#         self.discount = 10/100 

# class GoldCustomer(Customer):
#     def __init__(self,id,quantity,price):
#         Customer.__init__(self,id, quantity, price)
#         self.discount = 20/100


# customer_zero = Customer(2,10,100)
# print("Your bill amount is : ",customer_zero.generate_bill())

# customer_one = SilverCustomer(2,10,100)
# print("Your bill amount is : ",customer_one.generate_bill())

# customer_two = GoldCustomer(2,10,100)
# print("Your bill amount is : ",customer_two.generate_bill())








# class Employee:  
#     __count = 0;  
#     def __init__(self):  
#         Employee.__count = Employee.__count+1  
#     def display(self):  
#         print("The number of employees",Employee.__count)  
# emp = Employee()  
# emp2 = Employee()  
# try:  
#     print(emp.__count)  
# finally:  
#     emp.display() 







# class Employee:  
#     # __count = 0;  
#     def __init__(self):  
#         self.__count=0
#         self.__count =+1  
#     def display(self):  
#         print("The number of employees",self.__count)  
# emp = Employee()  
# emp2 = Employee()  
# try:  
#     print(emp.__count)  
# finally:  
#     emp.display()  





# class employee():
#     def __init__(self):
#         self.__maxearn = 1000000
#     def earn(self):
#         print("earning is:{}".format(self.__maxearn))
 
#     # def setmaxearn(self,earn):#//setter method used for accesing private class
#     #     self.__maxearn = earn
 
# emp1 = employee()
# emp1.earn()
 
# emp1.__maxearn = 10000
# emp1.earn()
 
# # emp1.setmaxearn(10000)
# # emp1.earn()





# class Account:
#     def __init__(self, account_number, account_balance):
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def withdraw(self, amount):
#         if self.account_balance - amount >= 0:
#             self.account_balance -= amount
#             print("Your Account Balance is: ", self.account_balance)
#         else:
#             print("Insufficient balance")

#     def deposit(self, depo):
#         if depo > 0:
#             self.account_balance += depo
#             print("Your Account Balance is: ", self.account_balance)

#     def display(self):
#         print("Account Number: {}".format(self.account_number))
#         print("Account Balance: {}".format(self.account_balance))

# # Create an empty list to store multiple accounts
# accounts = []

# while True:
#     print("\nChoose an action:")
#     print("1. Create Account")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Display Account Info")
#     print("5. Exit")

#     choice = input("Enter your choice (1/2/3/4/5): ")

#     if choice == '1':
#         account_number = input("Enter account number: ")
#         initial_balance = float(input("Enter the initial balance: "))
#         new_account = Account(account_number, initial_balance)
#         accounts.append(new_account)
#         print("Account created successfully!")
#     elif choice == '2':
#         account_number = input("Enter account number: ")
#         amount = float(input("Enter the amount to withdraw: "))
#         for account in accounts:
#             if account.account_number == account_number:
#                 account.withdraw(amount)
#             else:
#                 print("Account not found.")
#     elif choice == '3':
#         account_number = input("Enter account number: ")
#         deposit_amount = float(input("Enter the amount to deposit: "))
#         for account in accounts:
#             if account.account_number == account_number:
#                 account.deposit(deposit_amount)
#             else:
#              print("Account not found.")
#     elif choice == '4':
#         account_number = input("Enter account number: ")
#         for account in accounts:
#             if account.account_number == account_number:
#                 account.display()
#             else:
#                 print("Account not found.")
#     elif choice == '5':
#         break
#     else:
#         print("Invalid choice. Please choose a valid option.")







# class Account:
#     def __init__(self, account_number, account_balance):
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def withdraw(self, amount):
#         if self.account_balance - amount >= 0:
#             self.account_balance -= amount
#             print("Your Account Balance is: ", self.account_balance)
#         else:
#             print("Insufficient balance")

#     def deposit(self, depo):
#         if depo > 0:
#             self.account_balance += depo
#             print("Your Account Balance is: ", self.account_balance)

#     def display(self):
#         print("Account Number: {}".format(self.account_number))
#         print("Account Balance: {}".format(self.account_balance))

# # Create an empty dictionary to store multiple accounts
# accounts = {}

# while True:
#     print("\nChoose an action:")
#     print("1. Create Account")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Display Account Info")
#     print("5. Exit")

#     choice = input("Enter your choice (1/2/3/4/5): ")

#     if choice == '1':
#         account_number = input("Enter account number: ")
#         initial_balance = float(input("Enter the initial balance: "))
#         new_account = Account(account_number, initial_balance)
#         accounts[account_number] = new_account
#         print("Account created successfully!")
#     elif choice == '2':
#         account_number = input("Enter account number: ")
#         amount = float(input("Enter the amount to withdraw: "))
#         if account_number in accounts:
#             accounts[account_number].withdraw(amount)
#         else:
#             print("Account not found.")
#     elif choice == '3':
#         account_number = input("Enter account number: ")
#         deposit_amount = float(input("Enter the amount to deposit: "))
#         if account_number in accounts:
#             accounts[account_number].deposit(deposit_amount)
#         else:
#             print("Account not found.")
#     elif choice == '4':
#         account_number = input("Enter account number: ")
#         if account_number in accounts:
#             accounts[account_number].display()
#         else:
#             print("Account not found.")
#     elif choice == '5':
#         break
#     else:
#         print("Invalid choice. Please choose a valid option.")






# class Todolist:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print("Added task: ",task)

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             print("Removed task: ",task)
#         else:
#             print("Task not found in the to-do list.")

#     def show_tasks(self):
#         if not self.tasks:
#             print("No tasks in the to-do list.")
#         else:
#             print("To-Do List:")
#             for index, task in enumerate(self.tasks, 1):
#                 print("{}. {}".format(index,task))

# to_do_list = Todolist()

# while True:
#     print("\nOptions:")
#     print("1. Add Task")
#     print("2. Remove Task")
#     print("3. Show Tasks")
#     print("4. Exit")
#     choice = input("Enter your choice (1/2/3/4): ")

#     if choice == '1':
#         task = input("Enter the task: ")
#         to_do_list.add_task(task)
#     elif choice == '2':
#         task = input("Enter the task to remove: ")
#         to_do_list.remove_task(task)
#     elif choice == '3':
#         to_do_list.show_tasks()
#     elif choice == '4':
#         break
#     else:
#         print("Invalid choice. Please select a valid option.")







# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")

# class StudentManagementSystem:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)
#         print(f"Added student: {student.name}")

#     def remove_student(self, roll_number):
#         for student in self.students:
#             if student.roll_number == roll_number:
#                 self.students.remove(student)
#                 print(f"Removed student with Roll Number {roll_number}")
#                 return
#         print(f"Student with Roll Number {roll_number} not found.")

#     def display_students(self):
#         if not self.students:
#             print("No students in the system.")
#         else:
#             print("Student List:")
#             for student in self.students:
#                 student.display_info()

# student_system = StudentManagementSystem()

# while True:
#     print("\nOptions:")
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. Display Students")
#     print("4. Exit")
#     choice = input("Enter your choice (1/2/3/4): ")

#     if choice == '4':
#         break

#     if choice == '1':
#         name = input("Enter the student's name: ")
#         roll_number = input("Enter the student's roll number: ")
#         student = Student(name, roll_number)
#         student_system.add_student(student)
#     elif choice == '2':
#         roll_number = input("Enter the student's roll number to remove: ")
#         student_system.remove_student(roll_number)
#     elif choice == '3':
#         student_system.display_students()
#     else:
#         print("Invalid choice. Please select a valid option.")







# class Demo:
#     def add(self,*args):
#         total=0
#         for i in args:
#             total=total+i
#         return total

# d=Demo()
# print(d.add(2,3))
# print(d.add(1,2,3))
# print(d.add(3,4,5,6,7,8))







# # put unsafe operation in try block 
# try: 
#      print("code start") 
  
#      # unsafe operation perform 
#      print(1 / 0) 
# # if error occur the it goes in except block 
# except: 
#      print("an error occurs") 
# # final code in finally block 
# finally: 
#      print("always print") 






# x = 5
# y = "hello"
# try: 
# 	z = x + y 
# except TypeError: 
# 	print("Error: cannot add an int and a str") 





# a = [1, 2, 3] 
# try: 
# 	print ("Second element = " ,a[1]) 
# 	# Throws error since there are only 3 elements in array 
# 	print ("Fourth element = ",a[3]) 
# except IndexError: 
# 	print ("An error occurred")






# # try for unsafe code 
# try: 
#     amount = 1999
#     if amount < 2999: 
          
#         # raise the ValueError 
#         print("its an value error") 
#     else: 
#         print("You are eligible to purchase") 
              
# # if false then raise the value error 
# except ValueError: 
#         print() 





# # Program to handle multiple errors with one 
# # except statement 
# # Python 3 
# def fun(a): 
# 	if a < 6: 
# 		# throws ZeroDivisionError for a = 3 
# 		b = a/(a-3) 
# 	# throws NameError if a >= 4 
# 	print("Value of b = ", b) 
# try: 
# 	fun(3)
# 	fun(5) 

# # multiple exceptions 
# except ZeroDivisionError: 
# 	print("ZeroDivisionError Occurred and Handled") 
# except NameError: 
# 	print("NameError Occurred and Handled")






# def message():
# 	try:
# 		a = "hello"
# 		return b
# 	except NameError:
# 		return "NameError occurred. Some variable isn't defined."

# print(message())






# # Program to depict else clause with try-except 
# # Python 3 
# # Function which returns a/b 
# def abcd(a , b): 
# 	try: 
# 		c = ((a+b) / (a-b)) 
# 	except ZeroDivisionError: 
# 		print ("a/b result in 0") 
# 	else: 
# 		print (c) 
# # Driver program to test above function 
# abcd(2.0, 3.0) 
# abcd(3.0, 3.0)





# # Python program to demonstrate finally 
# # No exception Exception raised in try block 
# try: 
# 	k = 5//0 # raises divide by zero exception. 
# 	print(k) 
# # handles zerodivision exception 
# except Exception as e: 
# 	print("Can't divide by zero",{e}) 
# finally: 
# 	# this block is always executed 
# 	# regardless of exception generation. 
# 	print('This is always executed')






# try: 
# 	raise NameError("Hi there") # Raise Error 
# except Exception as e: 
# 	print ("An exception",{e}) 
# 	raise # To determine whether the exception was raised or not





# arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr)
# print(arr.ndim)



# import numpy as np
# arr1 = np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[1,2],[3,4]],[[5,6],[7,8]]]])
# print(arr1)
# print(arr1.ndim)


# arr1 = np.array([[1,2,3,4],[4,5,9,10]]) 
# print(arr1.shape)




# arr1 = np.array([[1,2,3,4],[4,5,9,10]]) 
# print(arr1.shape)




# arr1 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr1.shape)
# print(arr1.ndim)
# print(arr1.size)




# arr1 = np.array([1,2,3,4,5,6])
# print(arr1.dtype)



# arr1 = np.array([1,2,3,4,5,6,'abc'])
# print(arr1.dtype)



# my_array = np.array(['abd','bcd','abc'])
# print(my_array.dtype)




# Question 2: Create a Python class called Rectangle with attributes 
#             for length and width. Write a method to calculate the 
#             area of the rectangle.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#        return self.length * self.width

# # Example usage:
# a=float(input("enter the length : "))
# b=float(input("enter th width : "))
# my_rectangle = Rectangle(a,b)
# area = my_rectangle.calculate_area()
# print("Rectangle Area: {} square units".format(area))







# Question: Write a Python program that uses classes to implement a
#           simple menu-driven application. The program should include
#           classes for a Circle, Person, and Book, each with specific 
#           attributes and methods. The main part of the program should 
#           provide the user with a menu to choose from different options, 
#           such as calculating the properties of a circle, displaying person
#           details, displaying book information, or exiting the program. 
#           The user should be able to interact with the program by making choices
#           from the menu.

# Answer :

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14159265359 * self.radius ** 2

#     def calculate_circumference(self):
#         return 2 * 3.14159265359 * self.radius

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age} years")
#         print(f"Address: {self.address}")

# class Book:
#     def __init__(self, title, author, published_year):
#         self.title = title
#         self.author = author
#         self.published_year = published_year

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Published Year: {self.published_year}")

# while True:
#     print("\nOptions:")
#     print("1. Calculate Circle")
#     print("2. Display Person Details")
#     print("3. Display Book Info")
#     print("4. Exit")
#     choice = input("Enter your choice (1/2/3/4): ")

#     if choice == '4':
#         break 

#     if choice == '1':
#         radius = float(input("Enter the circle's radius: "))
#         my_circle = Circle(radius)
#         area = my_circle.calculate_area()
#         circumference = my_circle.calculate_circumference()
#         print(f"Circle Area: {area} square units")
#         print(f"Circle Circumference: {circumference} units")
#     elif choice == '2':
#         name = input("Enter the person's name: ")
#         age = int(input("Enter the person's age: "))
#         address = input("Enter the person's address: ")
#         person1 = Person(name, age, address)
#         person1.display_details()
#     elif choice == '3':
#         title = input("Enter the book's title: ")
#         author = input("Enter the book's author: ")
#         published_year = int(input("Enter the book's published year: "))
#         book1 = Book(title, author, published_year)
#         book1.display_info()
#     else:
#         print("Invalid choice. Please select a valid option.")








# class Shop:
#     def __init__(self, id, quantityitem, priceitem):
#         self.id = id
#         self.quantityitem = quantityitem
#         self.priceitem = priceitem

#     def gold(self):
#         total = self.priceitem * self.quantityitem
#         discount = total * 0.2
#         finalprice = total - discount

#         print(f"Price of an item: {total}")
#         print(f"Discount for gold customer: {discount}")
#         print(f"After discount: {finalprice}")

#     def silver(self):
#         total = self.priceitem * self.quantityitem
#         discount = total * 0.1
#         finalprice = total - discount

#         print(f"Price of an item: {total}")
#         print(f"Discount for silver customer: {discount}")
#         print(f"After discount: {finalprice}")

#     def exit(self):
#         print("Thank you for using the Billing System. Goodbye!")
#         exit()

# while True:
#     id = input("Enter your ID: ")
#     quantityitem = int(input("Enter quantity item: "))
#     priceitem = float(input("Enter price item: "))

#     print("Welcome to the Billing System")
#     print("1: Gold\n"
#           "2: Silver\n"
#           "3: Exit\n")
#     choice = input("Choose your customer type: ")

#     if choice == '3':
#         print("Thank you for using the Billing System. Goodbye!")
#         break
#     elif choice == '1':
#         shop = Shop(id, quantityitem, priceitem)
#         shop.gold()
#         while True:
#             print("1: Yes\n"
#                   "2: No\n")
#             cont = input("Do you want to continue? : ")
#             if cont == '2':
#                 shop.exit()
#             elif cont == '1':
#                 break
#     elif choice == '2':
#         shop = Shop(id, quantityitem, priceitem)
#         shop.silver()
#         while True:
#             print("1: Yes\n"
#                   "2: No\n")
#             cont = input("Do you want to continue? : ")
#             if cont == '2':
#                 shop.exit()
#             elif cont == '1':
#                 break
#     else:
#         print("Invalid choice. Please enter a valid option.")










# n = 6  # Change this to the number of rows you want in the triangle
# # Create the Pascal's triangle
# pascal_triangle = []
# for i in range(n):
#     current_row = [1]
#     if pascal_triangle:
#         previous_row = pascal_triangle[-1]
#         for j in range(len(previous_row) - 1):
#             current_row.append(previous_row[j] + previous_row[j + 1])
#         current_row.append(1)
#     pascal_triangle.append(current_row)

# # Find the maximum width for formatting
# max_width = len(' '.join(map(str, pascal_triangle[-1])))

# # Print the Pascal's triangle
# for row in pascal_triangle:
#     padding = max_width - len(' '.join(map(str, row)))
#     formatted_row = ' '.join(str(item) for item in row)
#     print(' ' * (padding // 2) + formatted_row + ' ' * (padding // 2))


# ouput:


# Pascal's triangle

#       1      
#      1 1     
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# 1 5 10 10 5 1




