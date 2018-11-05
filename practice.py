# import sys
# print(sys.version_info)


# print("Twinkle Twinkle little star \n\t\t How I wonder what you are! \n\t\t Up above the world so high, \n Like a diamond in the sky.")

# import datetime
# print(datetime.datetime.now())

# First_name = input("Please enter your first name")
# Last_name = input("Please enter your last name")
# user_name = Last_name +" " + First_name
# print(user_name)
#
# sample_data = 3,5,7,2,3
# My_list = []
# My_list.append(sample_data)
# print(My_list)
# My_tuple = ()
# My_tuple = tuple(sample_data)
# print(My_tuple)


# A = input("Enter a sample jpg file")
# print(A)
# output = A.split(".")
# print(output[-1])

# color_list = ["Red","Green","White" ,"Black"]
# # color_list = color_list[0] +" "+ color_list[-1]
# print(color_list)
# print(color_list[0:-1])



# exam_st_date = (11, 12, 2014)
# print("The examination will start on : %i/%i/%i" %exam_st_date)

#

# import calendar
# print(calendar.month(2018,10))
# #
# n = input("Enter any number")
# a = int(n)
# b = int(n+n)
# c = int(n+n+n)
# print(b)
# result = (a+b+c)
# print(result)

#(2014, 7, 2), (2014, 7, 11)
#
# from datetime import date
#
# f_date = date(2018,1,1)
# t_date = date(2018,8,11)
# t = t_date - f_date
# print(t.days)


# a = int(input("Enter the first number"))
# # b = int(input("Enter the second number"))
# # c = int(input("Enter the third number"))
# #
# # if a==b==c:
# #     d = 3*(a+b+c)
# # else:
# #     d = a+b+c
# # print("The result is %d" %d)

# stmt = input("write any sentence")
# if not stmt.startswith("is"):
#     stmt = "Is" + stmt
# print(stmt)

# input_string = "Hello"
# n_count = int(input("Enter the value of n"))
# for i in range(n_count):
#     print(input_string)

# my_list = [1,2,3,4,5,4,4,4]
# print(my_list.count(4))

# input_string = "Jas"
# n = int(3)
# if len(input_string)==1:
#     for i in range(3):
#         print(input_string)
# else:
#     for i in range(3):
#         input_string = input_string[0:2]
#         print(input_string)



# given_letter = input("Enter any letter")
# if not given_letter =="a" and "e" and "i" and "o" and "u":
#     print("this is not a vowel")
# else:
#     print("This is a vowel")

# my_list = [1,5,8,3]
# print(my_list.__contains__(5))

# my_list = [1,5,8,3]
# n = 3
# for i in my_list:
#     if n == i:
#         print("True,Number %i belongs to this list" %i)
#     else :
#         print("False")


# import multiprocessing
# print(multiprocessing.context)

# import getpass
# print(getpass.getuser())


# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
#
#
# numbers = [str(word) for word in numbers]
# print('-'.join(numbers))

# import subprocess
# subprocess.call(['ls',"-l"])










# my_list = []
#
# with open("hello.txt",'r') as fo:
#     for line in fo:
#         if "purpose" in line:
#             print(line)
#         my_list.append(line)



# for i in range(10):
#     print('*',end='-')
#
# def my_nonkeyarg(*args):
#     for i in args:
#         print(i)
#
# my_nonkeyarg('abc',1,False,'Hello',23.4)

# def my_keyarg(*args,**kwargs):
#     print(args)
#     for key,value in kwargs.items():
#         print(key,'=',value)
#
# my_keyarg('Hello',name='Gopi',age='33')
#


# def addition(a,b,c):
#     if (a==b or a==c or b==c):
#         result=0
#     else:
#         result = a+b+c
#     return result
#
# print(addition(2,2,5))


# def area_triangle(b,h):
#     area = 0.5*b*h
#     return area
#
# print(area_triangle(3,6))


# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# color_list_1_diff = color_list_1.symmetric_difference(color_list_2)
# print(color_list_1_diff)

# def simple(a,b):
#     if a == b or (a+b)==5 or (a-b)==5:
#         return "True"
#     else:
#         return "False"
#
# print(simple(9,2))
#
# a = "Hi"
# b = 11
# print(isinstance(b,int))

# a = 2
# b = 3.5
# if isinstance(a,int) and isinstance(b,int):
#     result = a+b
#     print("True and result is %d" %result)
# else:
#     print("False")


# import os.path
# open('C:\\Users\\Malathi_Jay\\Desktop\\pid_list.txt', 'r')
# print(os.path.isfile('pid_list.txt'))


# import struct
# print(struct.calcsize("P") * 8)

# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# import os
# print("Current File Name : ",os.path.realpath(__file__)


# import time
# t1 = time.time()
# print(t1)
# for i in range(100000):
#     x = i
# t2 = time.time()
# print(t2-t1)

# import datetime
# print(datetime.datetime.now())







# import re
#
# my_string = "Helloworld!"
# check = re.compile(r'\W')
# result = check.search(my_string)
# print(result)
# if result is bool:
#     print("special chars are there")
# else:
#     print("not availble")


# import os
#print(dir(os))
# print(os.getcwd())
# os.chdir('/Users/Malathi_Jay/PycharmProjects/jasvetha')
# print(os.getcwd())
# print(os.listdir())
# os.mkdir('assign1/subassign')
# os.removedirs('assign1/subassign')
# os.rename('','')
# print(os.stat)



# import numpy as np
# # a = np.array([(1,2,3),(4,5,6)])
# # print(a)
# # print(type(a))
#
# import sys
# s = range(1000)
# print(sys.getsizeof(6)*len(s))
#
# d = np.arange(1000)
# print(d.size*d.itemsize)
#
# import time
# size = 100000
# l1 = range(size)
# l2 = range(size)
#
# start = time.time()
#
# result = [(x,y) for x,y in zip(l1,l2)]
#
# print((time.time()-start)*1000)
#
#
# start = time.time()
# a1 = np.arange(size)
# a2 = np.arange(size)
# result = a1+a2
#
# print((time.time()-start)*1000)
#

# nterms = 15
# n1 = 0
# n2 = 1
# count = 0
#
# if nterms == 1:
#     print(n1)
# else:
#     while count<nterms:
#


# with open("loreum.txt") as f:
#     my_list =[]
#     for word in f:
#         print(word.split())
#         my_list.extend(word.split())
#
#
#     print(len(my_list))
#
#
# from collections import Counter
# count = Counter(my_list)
# # print(count)
# #print(len(count))
# my_set = set(my_list)
# print(my_set)
# print(len(my_set))



# def square(a,b):
#     result = ((a**2)+(b**2)+(2*a*b))
#     return result
# print(square(2,3))


# num_values = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
# # user_value = input("Enter any two digit")
# from itertools import product
#
# def combo(phnum):
#     return [''.join(tup) for tup in list(product(*[num_values[ch] for ch in phnum]))]
#
# print(combo('23'))


#
# import itertools
#
# letters_map = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL',
#                '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}
#
# def possible_words(phone_number):
#     letters_to_combine = (letters_map[digit] for digit in phone_number)
#     for letters_group in itertools.product(*letters_to_combine):
#         yield ''.join(letters_group)
#
# print(list(possible_words("23")))





# l1 = [1,2,4]
# l2 = [1,3,4]
# merge = l1+l2
# s = sorted(merge)
# print(s)
#
#
# def bracket_check(user_ip):
#     count = 0
#     for i in user_ip:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#     if count == 0:
#         return True
#     else:
#         return False
#
# print(bracket_check("((()))"))


# Given_nums = [0,0,1,1,1,2,2,3,3,4]
# print(set(Given_nums))

# a = [1,2,3,4,5]
# print(a[::-1])


# user_ip = "MAMA"
# if user_ip == user_ip[::-1]:
#     print("True")
# else:
#     print("False")

# import roman
# n=roman.toRoman(50)
# print(n)
#
# a = [1,2,3,5,7,9]
# print(a.index(7))

# a = [1,3,4,3,5,3,6,7]
# for index,value in enumerate(a):
#     print(index,value)
#     if value == 3:
#         a.pop(index)
# print(a)

import pandas as pd
df = pd.read_csv(r"C:\Users\Malathi_Jay\Desktop\FL_insurance_sample.csv")
# # print(df['eq_site_limit'].mean())
# df.fillna(0,inplace=True)
# print(df['eq_site_limit'][df['point_granularity']==3])
# df = pd.DataFrame([[1,2,3,4,5,6,7],[2,4,6,8,10,12,13,14]])
print(df.describe())







