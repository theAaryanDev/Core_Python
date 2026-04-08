#Lecture 9: Strings in python

str_1 = 'Type 1'
str_2 = "Type 2"
str_3 = """Type 3"""  #All three are same thing
spaced_str = "     Hello       My          Dear        Friends"

str_1[0] #string slicing
str_1.lower() #lower all char
spaced_str.strip() #removes spaces
chai = "Lemon Tea"
replaced_chai = chai.replace("Lemon", "Ginger") #work like Find-n-replace in str | always takes 2 arguments
print(replaced_chai)
print(chai) #NOTE: even after replacing; original string 'chai' never get change in memory

dhurandhar_array = "Hamza", "Rehman", "SP", "Yalina", "Arsad Pappu", "Major Iqbal", "Donga", "Ujjair", "Rayan"
print(type(dhurandhar_array)) #think-before-execute

str_4 = "apple"
print(str_4.split()) # 'apple' NOT 'a', 'p', 'p', 'l', 'e'
dhurandhar_str = "Hamza, Rehman, SP, Yalina, Arsad Pappu, Major Iqbal, Donga, Ujjair, Rayan"
print(type(dhurandhar_str))
print(dhurandhar_str.split()) #split on basis of default parameter (i.e. space " ")
print(dhurandhar_str.split(", ")) #split on the basis of ", " (comma-one space)
print(dhurandhar_str.split(",")) #split on the basis of "," (comma-only)
print(dhurandhar_str.find("SP")) #find and retuen index ; -1 if not found

repetitive_str = "apple ball ball ball cat dog"
print(repetitive_str.count("ball")) #count() of ball in str

chai_type = "Masala"
qty = 2
order = "I ordered {} cups of {} chai." #{} are called placeholders
print(order.format(qty, chai_type)) # .format()

#---------------List to str conversion---------------------
chai_variety = ["Masala", "Lemon", "Ginger", "Black"]
chai_variety_str = " and ".join(chai_variety) #you can pass the custum seperator inside double quotes "" 
print(chai_variety_str)

#NOTE: 1. \n : new line (Backslash-n)    2. \" is treated is " (Backslash-double-inverted)

#how to write str? : "He said, "masala chai is awesome." "
chai_statement = "He said, \"Masala Chai is Awesome\""
print(chai_statement)

#How to print path od directory? c:\Aryan\TheAryanDev\new_folder\ (Make sure \n of 'new_folder' must not treated as new line syntax)
#print("c:\Aryan\TheAryanDev\new_folder\") #error
print("c:\\Aryan\\TheAryanDev\\new_folder\\") #Method 1
print(r"c:\Aryan\TheAryanDev\new_folder") #Method 2 : Use raw i.e. r before string (But has a limitation: can't use \ in the end. see below ↓)
# print(r"c:\Aryan\TheAryanDev\new_folder\") #error (bcz.. \ in the end) | can't even write comment in this line.
#But more developers use raw string method (Method : 1)

print("Lemon" in chai)