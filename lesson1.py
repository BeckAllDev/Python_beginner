# Variable and string
# print("Hello World!!!")
# print("Hello World !!!")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
# print('og\'abek')
# phrase="hello world"
# print(phrase.lower())
# print(phrase.islower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase[0])
# numbers=123
# str1=str(numbers)
# s=0
# for i in str1:
# 	s+=int(i)
# print(s)

# phrase1="Hammasi joyida deb aytgandilar "
# print(phrase1.index("d"))
# print(phrase1.replace("Hammasi","Barchasi"))
# using numbers
# print(10%3) #modulus
# number=-5
# print(abs(-5)) #modul
# print(str(number)+"  is favourt number") #number is int replace string str()
# print(pow(3,4))#degree
# print(max(10,5))#maximal number
# print(round(3.2))
# print(round(3.7))
# from math import *
# print(floor(3.2))
# print(floor(3.7))
# print(ceil(3.2))
# print(ceil(3.7))
# print(sqrt(64))

# name=input("What is your name?:")
# print(name)
#
# num1=input("number1:")
# num2=input("number2:")
# result=int(num1)+int(num2)
# print(result)
# List
# friends=["John","Isobek","Bunyod"]
# friends2=["Aziz","Shuxrat"]
# friends.extend(friends2)
# friends.append("Norboy")
# friends.insert(1,"Sarvar")
# friends.remove("Aziz")
# print(friends)
# Functions

# def say_hi(name, age):
#     print(f"Hello {name} ,you are {age}")
#
#
# name1 = input("What is your name?:")
# age1 = input("How old you?:")
# say_hi(name1, age1)

# def cube(number):
#     return number*number*number
# num=int(input("number:"))
# print(cube(num))

# is_male=input("is male:")
# is_tall=int(input("is tall:"))
# if is_male.lower()=="erkak" and is_tall>=175:
#     is_male=True
#     is_tall=True
# if is_male and is_tall:
#     print("He is male and He is Tall")
# else:
#     print("She is female and She is short")
# def max_num(num1,num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(-6,10,0))

# using While

# key_word = "123456789"
# password = ""
# password_count = 0
# password_limit = 3
# out_of_password = False
# while key_word != password and not out_of_password:
#     if password_count < password_limit:
#         password = input("Please!enter your password:")
#         password_count += 1
#     else:
#         out_of_password = True
# if out_of_password:
#     print("Out of password,password incorrect")
# else:
#     print("Password correct")

# def raise_to_power(base_num,pow_num):
#     result=1
#     for index in range(pow_num):
#         result=result*base_num
#     return result
# print(raise_to_power(10,2))
# Lists &Nested loops
# number_grid=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)

# Build a Translator
# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + 'G'
#             else:
#                 translation = translation + 'g'
#
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translate(input("Enter a phrase:")))

#Try Except

# try:
#     #value=10/0
#     number =int(input("Enter a number:"))
#     print(number)
# except ZeroDivisionError as zer:
#     print(zer)
# except ValueError as ve:
#     print(ve)

#REading Files
# filename=open("employees1.txt","w")
#
# filename.write("\nBekhzod - Bunyod")
# # for i in filename.readlines():
# #     print(i)
# filename.close()

