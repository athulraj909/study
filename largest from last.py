
# n = int(input("Enter the number of elements: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i + 1}: ")) 
#     numbers.append(num)
# while True:
#     k = int(input("Enter the number of largest numbers to find: "))
#     if k>n:
#         break
#     else: 
#         largest_numbers = sorted(numbers, reverse=True)[:k]

#         print(f"The {k} largest numbers are: {largest_numbers}")
    
    





# n = int(input("Enter the number of elements: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i + 1}: ")) 
#     numbers.append(num)
# k = int(input("Enter the number of largest numbers to find: ")) 
# largest_numbers = sorted(numbers,reverse=True)[:k]

# print(f"The {k} largest numbers are: {largest_numbers}")







# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Input: Taking the year as input
# user_year = int(input("Enter a year to check if it's a leap year: "))
# if is_leap_year(user_year):
#     print(f"{user_year} is a leap year!")
# else:
#     print(f"{user_year} is not a leap year.")




# # GCD of numbers:

# def find_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Input: Taking two numbers as input
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# gcd_result = find_gcd(num1, num2)
# print(f"The GCD of {num1} and {num2} is: {gcd_result}")




# # Sum of Digits:

# num = int(input("Enter a number: "))
# sum_of_digits = 0

# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num //= 10

# print("Sum of the digits:", sum_of_digits)



# # multiplication table:

# num = int(input("Enter a number: "))
# multiplier = 1

# while multiplier <= 10:
#     product = num * multiplier
#     print(f"{num} * {multiplier} = {product}")
#     multiplier += 1





# # Binary to Decimal Conversion:

# binary = input("Enter a binary number: ")
# decimal = 0
# power = len(binary) - 1
# index = 0

# while index < len(binary):
#     digit = int(binary[index])
#     decimal += digit * (2 ** power)
#     power -= 1
#     index += 1

# print("Decimal equivalent:", decimal)





# # Linear Search in a List:

# def linear_search(lst, target):
#     index = 0
#     while index < len(lst):
#         if lst[index] == target:
#             return index
#         index += 1
#     return -1

# my_list = []
# my = int(input("enter how many elements : "))
# for i in range(my):
#     a = int(input(f"Enter the number {i+1} : "))
#     my_list.append(a)

# target = int(input("Enter the number to search for: "))
# result = linear_search(my_list, target)
# if result != -1:
#     print(f"{target} found at index {result}.")
# else:
#     print(f"{target} not found in the list.")



# # Checking Armstrong Numbers:

# def is_armstrong(num):
#     temp = num
#     order = len(str(num))
#     armstrong_sum = 0
#     while temp > 0:
#         digit = temp % 10
#         armstrong_sum += digit ** order
#         temp //= 10
#     return num == armstrong_sum

# number = int(input("Enter a number: "))
# if is_armstrong(number):
#     print(number, "is an Armstrong number.")
# else:
#     print(number, "is not an Armstrong number.")





# # Printing Pascal's Triangle:

# def generate_next_row(row):
#     next_row = [1]
#     for i in range(len(row) - 1):
#         next_row.append(row[i] + row[i + 1])
#     next_row.append(1)
#     return next_row
# rows = int(input("Enter the number of rows for Pascal's triangle: "))
# current_row = [1]
# for _ in range(rows):
#     print(current_row)
#     current_row = generate_next_row(current_row)



# # vehicle
# a = []

# def add():
#     n = int(input("Enter how many pairs: "))
#     for i in range(n):
#         name = input("Enter your vehicle: ")
#         if any(name in vehicle for vehicle in a):
#             print(f"{name} already exists")
#         else:
#             price = int(input("Enter your vehicle price: "))
#             wheel = int(input("How many wheels: "))
#             a.append([name, price, wheel])
#             print(a)

# def display():
#     def two():
#         print("Two-wheel vehicles:")
#         for vehicle in a:
#             if vehicle[2] == 2:
#                 print(f"{vehicle[0]} - Price: {vehicle[1]}")

#     def three():
#         print("Three-wheel vehicles:")
#         for vehicle in a:
#             if vehicle[2] == 3:
#                 print(f"{vehicle[0]} - Price: {vehicle[1]}")

#     def four():
#         print("Four-wheel vehicles:")
#         for vehicle in a:
#             if vehicle[2] == 4:
#                 print(f"{vehicle[0]} - Price: {vehicle[1]}")

#     while True:
#         print("1: Two-wheel\n"
#               "2: Three-wheel\n"
#               "3: Four-wheel\n"
#               "4: Exit\n")
#         choice = int(input("Enter your choice: "))
#         if choice == 4:
#             break
#         elif choice == 1:
#             two()
#         elif choice == 2:
#             three()
#         elif choice == 3:
#             # Define the 'four' function if needed
#             four()

# while True:
#     print("1: Add\n"
#           "2: Display\n"
#           "3: Exit\n")
#     choice = int(input("Enter your choice: "))
#     if choice == 3:
#         break
#     elif choice == 1:
#         add()
#     elif choice == 2:
#         display()





# # student
# students = []
# def add_student():
#     n = int(input("Enter the number of students: "))
#     for i in range(n):
#         student = {}  # Initialize student dictionary for each iteration
#         name = input("Enter student's name: ")
#         for s in students:
#             if name in s['name'] :
#                 print(f"{name} already exists")
#         else:
#             subjects = {}
#             for subject in ['Maths', 'Science', 'English']:
#                 score = float(input(f"Enter {subject} score for {name}: "))
#                 subjects[subject] = score
#             student['name'] = name
#             student['subjects'] = subjects
#             students.append(student)
#             print(students)

# def display_students():
#     while True:
#         print("1: Display Maths scores\n"
#               "2: Display Science scores\n"
#               "3: Display English scores\n"
#               "4: Exit\n")
#         choice = int(input("Enter your choice: "))
#         if choice == 4:
#             break
#         elif choice == 1:
#             display_subject_scores('Maths')
#         elif choice == 2:
#             display_subject_scores('Science')
#         elif choice == 3:
#             display_subject_scores('English')

# def display_subject_scores(subject):
#     print(f"{subject} scores:")
#     for i in students:
#         print(f"{i['name']}: {i['subjects'][subject]}")

# while True:
#     print("1: Add Student\n"
#           "2: Display Students\n"
#           "3: Exit\n")
#     choice = int(input("Enter your choice: "))
#     if choice == 3:
#         break
#     elif choice == 1:
#         add_student()
#     elif choice == 2:
#         display_students()






# a = []
# def add():
#     b = []
#     n = int(input("Enter how many pairs: "))
#     for i in range(n):
#         name = input("Enter your vehicle name: ")

#         if name in b:  # Check if name already exists
#             print(f"{name} already exists")
#         else:
#             price = int(input("Enter your vehicle price: "))
#             wheel = int(input("How many wheels: "))
#             b = [name, price, wheel]  # Create a new list for each vehicle
#             a.append(b)
#             print(b)
#             print(a)

# def display():
#     def two():
#         for vehicle in a:
#             if vehicle[2] == 2:
#                 print(f"{vehicle[0]} is a two wheel vehicle.price is {vehicle[1]}")

#     def three():
#         for vehicle in a:
#             if vehicle[2] == 3:
#                 print(f"{vehicle[0]} is a three wheel vehicle")

#     def four():
#         for vehicle in a:
#             if vehicle[2] == 4:
#                 print(f"{vehicle[0]} is a four wheel vehicle")

#     while True:
#         print("1: Two-wheel \n"
#               "2: Three-wheel\n"
#               "3: Four-wheel\n"
#               "4: Exit\n")
#         y = int(input("Enter your choice: "))
#         if y == 4:
#             break
#         elif y == 1:
#             two()
#         elif y == 2:
#             three()
#         elif y == 3:
#             four()

# while True:
#     print("1: Add \n"
#           "2: Display\n"
#           "3: Exit\n")
#     y = int(input("Enter your choice: "))
#     if y == 3:
#         break
#     elif y == 1:
#         add()
#     elif y == 2:
#         display()




# def display4(d):
#   f=0
#   vowels = ["a", "e", "i", "o", "u"]
#   count=0
#   for character in d:
#     if character in vowels:
#       count += 1
#       f=1
#   if f==0:
#     print("no vowels")
#   else:
#     print("number of vowels are :",count)
# d=input("enter the number :")
# display4(d)




# def display_vowels(d):
#     vowels = ["a", "e", "i", "o", "u"]
#     found_vowels = []
#     for character in d:
#         if character in vowels:
#             found_vowels.append(character)
#     if not found_vowels:
#         print("No vowels found.")
#     else:
#         print("Vowels found:", ", ".join(found_vowels))

# d = input("Enter the string: ")
# display_vowels(d)



# print("Enter the size of the array: ", end="")
# N = int(input())

# print("Enter the elements of the array:")
# Arr = []
# for i in range(N):
#     num = int(input(f"Enter the {i+1} element : "))
#     Arr.append(num)

# sum_odd = 0
# for num in Arr:
#     if num % 2 != 0:
#         sum_odd += num

# print("Sum of odd elements:", sum_odd)




# import calendar;  
# cal = calendar.calendar(2024)     
# print(cal)






# Ascending And Descending Sort Halves    30min
# You are given an array of integers. Your task is to sort the first half of the array 
# in ascending order and the second half in descending order.

# d = int(input("how many elements: "))
# arr = []
# for i in range(d):
#     input_str = input(f"enter the {i+1} number: ")
#     split_input = input_str.split()
#     for x in split_input:
#         arr.append(int(x))


# arr.sort()
# mid = len(arr) // 2
# first_half = arr[:mid]
# second_half = arr[mid:]

# first_half.sort()


# second_half.sort(reverse=True)

# sorted_arr = first_half + second_half

# print(sorted_arr)







# n = int(input("Enter how many number : "))
# nums = []
# for i in range(n):
#     a = input(f"Enter the {i+1} number : ")
#     b = []
#     b.append(a)
#     for x in b:
#         nums.append(int(x))
# total_sum = sum(nums)
# output = []
# for i in nums:
#     output.append(total_sum - i)
# print(output)




# # Swapping
# a=10
# b=20
# print("before swapping")
# print("a = ",a)
# print("b= ",b)
# a+=b
# b=a-b
# a=a-b
# print("after swapping")
# print("a = ",a)
# print("b = ",b)



# first missing positive number
# # Input the number of integers
# n = int(input("Enter the number of integers: "))

# # Input the integers
# arr = []
# print("Enter the integers:")
# for _ in range(n):
#     num = int(input())
#     arr.append(num)

# # Apply the algorithm to find the smallest missing positive integer
# i = 0
# while i < n:
#     if 0 < arr[i] <= n and arr[arr[i] - 1] != arr[i]:
#         # Swap arr[i] to its correct position
#         temp = arr[arr[i] - 1]
#         arr[arr[i] - 1] = arr[i]
#         arr[i] = temp
#     else:
#         i += 1

# # Find the first missing positive integer
# for i in range(n):
#     if arr[i] != i + 1:
#         print("Output:", i + 1)
#         break
# else:
#     print("Output:", n + 1)









# # Duplicates element in array
# arr = []  
# a = int(input("Enter how many numbers : "))
# for i in range(a):
#     b = int(input(f"Enter the {i+1} number : "))
#     arr.append(b)

# array = []
# #Searches for duplicate element    
# for i in range(0, len(arr)):    
#     for j in range(i+1, len(arr)):    
#         if(arr[i] == arr[j]):    
#             array.append(arr[j])  

# if array:
#     print("True")
# else:
#     print("False")



# # Anagram
# a = input("Enter the first string : ")
# b = input("Enter the second string : ")

# if sorted(a) == sorted(b):
#     print("Yes")
# else:
#     print("No")




# class Shop:
#     def __init__ (self,id,quantityitem ,priceitem):
#         self.id=id
#         self.quantityitem=quantityitem
#         self.priceitem=priceitem
 
#     def gold(self):
#         total=priceitem*quantityitem
#         discount = total* 0.2
#         finalprice=total-discount
#         print(f"Price of a item : {total}")
#         print (f"Discode for gold customer : {discount}")
#         print (f" After discode  : {finalprice}")
#     def silver(self):
#         total=priceitem*quantityitem
#         discount = total* 0.1
#         finalprice=total-discount
#         print(f"Price of a item : {total}")
#         print (f"Discode for gold customer : {discount}")
#         print (f" After discode  : {finalprice}")
#     def exit(self):
#         print("Thank you for using the Billing System. Goodbye!")
#         exit()   
    

    

# while True:
#         id=int(input("enter your id : "))
#         quantityitem=int(input("enter quantity iteam :"))
#         priceitem=int(input("enter price iteam : "))
#         print("Welcome to the Billing System")
#         print("1:gold\n"
#               "2:silver \n"
#               "3:exit \n")
#         x=int(input("Choose your customer type : "))
#         if x==3:
#             print("Thank you for using the Billing System. Goodbye!")
#             break
#         elif x==1:
#             a=Shop(id, quantityitem, priceitem)
#             a.gold()
#             while True:
#                 print("1:yes\n"
#                     "2:no \n")
#                 x=int(input("Do you want to continue? : "))
#                 if x==2:
                    
#                     a.exit()
#                 elif x==1:
#                     break
                
#         elif x==2:
#             a=Shop(id, quantityitem, priceitem)
#             a.silver()
#             while True:
#                 print("1:yes\n"
#                     "2:no \n")
#                 x=int(input("Enter your choice : "))
#                 if x==2:
#                     a.exit()      
#                 elif x==1:
#                     break
#                 else:
#                     print("Invalid choice. Please enter a valid option.")