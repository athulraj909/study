# n=7
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1:
#             print("1",end=" ")
#         else:
#             print("0", end=" ")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         if j==1:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         print()


# n=10

# for i in range(n):
#     for j in range(n - i):
#         if j < n - i - 1:
#             print(" ",end="")
#         else:
#             print("7", end="")
#     print()



# def display_number_7_pattern():
#     pattern = [
#         "7777777777777",
#         "            7",
#         "           7",
#         "          7",
#         "         7",
#         "        7",
#         "       7",
#         "      7",
#         "     7",
#         "    7",
#         "   7",
#     ]

#     for line in pattern:
#         print(line)

# display_number_7_pattern()



# rows = 7

# # Print the upper part of the pyramid
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("1", end=' ')
#     print()

# # Print the lower part of the pyramid
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("0", end=' ')
#     print()






# i=1
# while i<=10:
#     print(i)
#     i+=1


# my_tuple = ('a', 'p', 'p', 'l', 'e')
# print(my_tuple.count('p'))  
# print(my_tuple.index('l'))  

# a=set([1,2,"python"])
# print(type(a))
# for i in a:
#     print(i)


# n=input("enter the input : ")
# a=n[::-1]
# if n==a:
#     print("it is paliandrome ")
# else:
#     print("it is not palinadrome")



# a = int(input("Enter the start of the range: "))
# b = int(input("Enter the end of the range: "))

# sum_even = 0

# for num in range(a, b + 1):
#     if num % 2 == 0:
#         sum_even += num

# print("The sum of even numbers in the range from {} to {} is {}".format(a,b,sum_even))



# score = int(input("enter the mark : "))
# if score >= 100:
#     print("invalid mark")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# while True:
#     score = int(input("Enter a score (or -1 to quit): "))

#     if score == -1:
#         break  # Exit the loop if -1 is entered
#     if score >100:
#         print("invalid mark")
#     elif score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 70:
#         print("C")
#     elif score >= 60:
#         print("D")
#     else:
#         print("F")



# numbers = [1, 2, 3, 4, 5]
# a = [x ** 2 for x in numbers]
# print(a)



# List = [character for character in [1, 2, 3]]
# # Displaying list
# print(List)



# list = [i for i in range(10) if i % 2 == 0]
# print(list)



# matrix = [[j for j in range(3)] for i in range(3)]  
# print(matrix)



# matrix = []
# for i in range(3):
# 	# Append an empty sublist inside the list
# 	matrix.append([])
# 	for j in range(3):
# 		matrix[i].append(j)
# print(matrix)



# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  
# myDict = { k:v for (k,v) in zip(keys, values)}  
# # myDict = dict(zip(keys, values))  
# print (myDict)


# List = [character for character in [1, 2, 3]]
# print(List)





# x=int(input("enter : "))
# for i in range(x,0,-1):
#     if i==x:
#         print(" "+"*"*(x-5)+" "*3+"*"*(x-5))
#     elif i==x-1:
#         print("*"*(x-3)+" "+"*"*(x-3))
#     else:
#         print(" "*((x-2)-i)+"*"*i+"*"*(i-1))

