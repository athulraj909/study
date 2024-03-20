# class Student:  
#     def __init__(self, name, id, age):  
#         self.name = name  
#         self.id = id  
#         self.age = age  
  
#     # creates the object of the class Student  
# s = Student("John", 101, 22)  
  
# # prints the attribute name of the object s  
# print(getattr(s, 'name'))  
  
# # reset the value of attribute age to 23  
# setattr(s, "age", 23)  
  
# # prints the modified value of age  
# print(getattr(s, 'age'))  
  
# # prints true if the student contains the attribute with name id  
  
# print(hasattr(s, 'id'))  
# # deletes the attribute age  
# delattr(s, 'age')  
  
# # this will give an error since the attribute age has been deleted  
# print(s.age)  











# # single inheritance

# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# #child class Dog inherits the base class Animal  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
# d = Dog()  
# d.bark()  
# d.speak()  







# # multi-level inheritance

# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# #The child class Dog inherits the base class Animal  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
# #The child class Dogchild inherits another child class Dog  
# class DogChild(Dog):  
#     def eat(self):  
#         print("Eating bread...")  
# d = DogChild()  
# d.bark()  
# d.speak()  
# d.eat()  









# # multiple inheritance

# class Calculation1:  
#     def Summation(self,a,b):  
#         return a+b
# class Calculation2:  
#     def Multiplication(self,a,b):  
#         return a*b 
# class Derived(Calculation1,Calculation2):  
#     def Divide(self,a,b):  
#         return a/b
# d = Derived()  
# print(d.Summation(10,20))  
# print(d.Multiplication(10,20))  
# print(d.Divide(10,20)) 











# # Hierarchical  inheritance

# # Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
# # Derived class1
# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")
# # Derivied class2
# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()












# # polymorphism

# class Animal:  
#     def speak(self):  
#         print("speaking")  
# class Dog(Animal):  
#     def speak(self):  
#         print("Barking")  
# d = Dog()  
# d.speak()











# class Bank:  
#     def getroi(self):  
#         return 10;  
# class SBI(Bank):  
#     def getroi(self):  
#         return 7;  
# class ICICI(Bank):  
#     def getroi(self):  
#         return 8;  
# b1 = Bank()  
# b2 = SBI()  
# b3 = ICICI()  
# print("Bank Rate of interest:",b1.getroi());  
# print("SBI Rate of interest:",b2.getroi());  
# print("ICICI Rate of interest:",b3.getroi())

















# class Bird:
#     def intro(self):
#             print("There are many types of birds.")
#     def flight(self):
#             print("Most of the birds can fly but some cannot.")
# class sparrow(Bird):
#     def flight(self):
#             print("Sparrows can fly.")
# class ostrich(Bird):
#     def flight(self):
#             print("Ostriches cannot fly.")
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_spr.intro()
# obj_spr.flight()
# obj_ost.intro()
# obj_ost.flight()






