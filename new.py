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
# 		# print (self.__hiddenVariable) 

# # Driver code 
# myObject = MyClass()	 
# myObject.add(2) 
# myObject.add(5) 

# # This line causes error 
# print (myObject.__hiddenVariable) 






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
# 		# print(self.__c)

# class Derived(Base): 
# 	def __init__(self): 

# 		Base.__init__(self) 
# 		print("Calling private member of base class: ") 
# 		print(self.__c) 

# # Driver code 
# obj1 = Base() 
# # print(obj1.__c)
# # print(obj1.a) 
# # obj2=Derived()
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

# customer_two = GoldCustomer(3,10,100)
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







class Account:
    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def withdraw(self, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            print("Your Account Balance is: ", self.account_balance)
        else:
            print("Insufficient balance")

    def deposit(self, depo):
        if depo > 0:
            self.account_balance += depo
            print("Your Account Balance is: ", self.account_balance)

    def display(self):
        print("Account Number: {}".format(self.account_number))
        print("Account Balance: {}".format(self.account_balance))

# Create an empty dictionary to store multiple accounts
accounts = {}

while True:
    print("\nChoose an action:")
    print("1. Create Account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Display Account Info")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter the initial balance: "))
        new_account = Account(account_number, initial_balance)
        accounts[account_number] = new_account
        print("Account created successfully!")
    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        if account_number in accounts:
            accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")
    elif choice == '3':
        account_number = input("Enter account number: ")
        deposit_amount = float(input("Enter the amount to deposit: "))
        if account_number in accounts:
            accounts[account_number].deposit(deposit_amount)
        else:
            print("Account not found.")
    elif choice == '4':
        account_number = input("Enter account number: ")
        if account_number in accounts:
            accounts[account_number].display()
        else:
            print("Account not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please choose a valid option.")





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
# except ZeroDivisionError: 
# 	print("Can't divide by zero") 
# finally: 
# 	# this block is always executed 
# 	# regardless of exception generation. 
# 	print('This is always executed')






# try: 
# 	raise NameError("Hi there") # Raise Error 
# except NameError: 
# 	print ("An exception") 
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



