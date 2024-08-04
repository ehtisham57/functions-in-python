# functions in python

# no 1 
# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()
# my_function()
# my_function()

# no 2 Square

# num = eval(input("Enter a number: "))
# def square():
#     return num * num

# print(square())

# no 3 Cube

# num = eval(input("Enter a number: "))
# def Cube():
#     return num * num *num

# print(Cube())

# no 4 increment

# def inc(val):
#     for i in range(1, val +1):
#         print("H " * i)
# inc(5)

# no 5 decrement
# def dec(val):
#     for i in range(val, 0, -1):
#         print("A " * i)
# dec(5)

# no 5 All even

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# def AllEven(lst):
#     return [x for x in lst if x % 2 == 0]

# even_numbers = AllEven(li)
# print(even_numbers) 

# no 6 All Odd


# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# def AllOdd(lst):
#     return [x for x in lst if x % 2 != 0]

# even_numbers = AllOdd(li)
# print(even_numbers) 

# no 7 quadratic function 

# import math

# a = eval(input("Enter the value of a: "))
# b = eval(input("Enter the value of b: "))
# c = eval(input("Enter the value of c: "))

# def Qudr(a,b,c):
#     discriminant = b**2 - 4*a*c
#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2*a)
#         root2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return root1, root2
#     elif discriminant == 0:
#         root = -b / (2*a)
#         return root, None
#     else:
#         return None, None
# roots = Qudr(a, b, c)
# print(f"The roots of the quadratic function are {roots}")


# no 8 vowel 

# charlist = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'y', 'z']
# def vowels(charlist):
#     vowels = "aeiouAEIOU"
#     for char in charlist:
#         if char in vowels:
#             print(char)

# vowels(charlist)

# no 9 Checkcircle

# x = eval(input("Enter the value of x: "))
# y = eval(input("Enter the value of y: "))
# r = eval(input("Enter the value of r: "))

# def checkCircle(x,y,r):
#     SquarePoint = x * x + y * y
#     radius = r * r 
#     if SquarePoint < radius:
#         return "inside"
#     elif SquarePoint == radius:
#         return "on the boundary"
#     else:
#         return "outside"
# result = checkCircle(x , y, r)
# print(result) 

# no 10  Iterate over each number in the list

# for num in range(2):
#     print(num, end = ' ')
# for num in range(1):
#     print(num, end=' ')
# for num in range(3, 7):
#     print(num, end=' ')
# for num in range(1, 2):
#     print(num, end=' ')
# for num in range(0, 4, 3):
#     print(num, end=' ')
# for num in range(5, 22, 4):
#     print(num, end=' ')