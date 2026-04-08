#Lec 8: Numbers in depth in python

x = 2 
y = 3 
z = 4
print(x + y * z)  #this type of code practice rejected in production-level code reviews
print((x + y) * z) #here, priorities cleared with parenthesis ().

print(40 + 10.25) #no error BUT wrong practice
print(float(40) + 10.25) #right practice
print('Aryan ' + str(45)) #right practice

print('chai' + 'code') #chaicode ; operator overloading (basic grammar of program)

# print (type(x, y, z)) #error
print (x, y, z) #(2, 3, 4) ; when you print multiple values simultaneously , python group those in tuple format "() NOT []/{}""

#Assignment:
repr("Chai") #"'chai'" (print in terminal to see output)
str("Chai") #'chai' (print in terminal to see output)
print("chai") #chai 
#Understand the difference b/w these three. 

import math
print(math.floor(3.6)) #3 
print(math.floor(-3.6)) #-4 (NOTE: floor() always takes towards bottom value.)
print(math.trunc(3.6)) #3
print(math.trunc(-3.6)) #-3 (while, trunc() always takes towards '0' on the number line)
print(math.ceil(3.2)) #4
print(math.ceil(-3.2)) #-3

#------------oct / hex / bin / imaginary ----------------------
print((3+1j) * 3) #3+1j (imaginary numbers can also be handles in py)
print(0o20) #octal representation
print(0xFF) #hexal 
print(0b1000) #bin

#Reverse of line (34/35/36)
oct(64) #gives oct of 64  #method 2 : int('64', 8)
hex(64) #gives hexa of 64 #method 2 : int('64', 6)
bin(64) #gives bin of 64 #method 2 : int('64', 2)


int('64', 8) #means octal of 64
int('64', 12)    #means base-12 of 64
int('10000', 2) #means binary of 10000 , BUT cross-verify this technques. i have doubt

#--------------Bitwise operation in python (read from mdn)----------Chai&Code didn't teach about this-----------
x= 545454
y = x << 2 #bitwise operation look like this 
print(x)
print(y)
#Assignment: Understand how bitwise works?

import random
random_number = random.random()
# random_int = random.randint()  #without argument, not allowed; must paased some arguments
random_int_within_range = random.randint(0, 100)
print(random_number)
# print(random_int)
print(random_int_within_range)

dhurandhar_array = ["Hamza", "Rehman", "SP", "Yalina", "Arsad Pappu", "Major Iqbal", "Donga", "Ujjair", "Rayan"]
print(random.choice(dhurandhar_array)) #random.choice() choose randomly from an array or list.
random.shuffle(dhurandhar_array) #random.shuffle() shuffle the array or list.
print(dhurandhar_array) #shuffled array will be printed

#NOTE: Array() store same data types, List() stores different data types.

#-------------------------Decimal---------------------
print(0.1 + 0.1 + 0.1)  #print and see result
print((0.1 + 0.1 + 0.1) - 0.3) #print and see result
#these are the known python problems, to fix these problem, we use import statement dor decimal and fraction the use
from decimal import Decimal
correct_decimal_addition = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
correct_decimal_substraction = (Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3')
print(correct_decimal_addition)
print(correct_decimal_substraction)

from fractions import Fraction
fraction_a = Fraction(1,2)  #means 1/2
fraction_b = Fraction(1,2)  #means 1/2
print(fraction_a + fraction_b)

#------------------------set--------------------
set_one = {1, 2, 3, 4, 5, 6}
set_two = {1, 3, 4, 6, 8, 0}

intersection_set = set_one & set_two #intersection
union_set = set_one | set_two #union
difference_of_set_1 = set_one - set_two #difference
difference_of_set_2 = set_two - set_one #difference

print(intersection_set)
print(union_set)
print(difference_of_set_1)
print(difference_of_set_2)

print(set_one - set_one) #'set()' NOT '{}' (because type(set()) = set BUT type({}) = dict)
#-------------------------------------------------------

print(True + 5) #6 (True treated as 1 in py)
