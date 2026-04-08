#Lecture 20: Python Project - Youtube manager app


#------------------------------------------------------ enumerate method start -------------------------------------------------
chai_tuple = ("Masala", "Ginger", "Lemon")
chai_enum_value = enumerate(chai_tuple)
chai_list = list(chai_enum_value)
print(chai_list) #DryRun | list(enumerate(tuple)) VS list(tuple)

chai_list_direct = list(chai_tuple)
print(chai_list_direct) #DryRun | list(enumerate(tuple)) VS list(tuple)
#---------------------------------------------------------- enumerate method end -----------------------------------------------

#-----------------------------------------------------error handling start------------------------------------------------------------
#file opening method 1
# file = open('youtube.txt', 'w') #'w' → write mode | Also, 'w' → if file NOT exist; automatically created 

# try:
#     file.write('chai aur code')
# except FileNotFoundError:   #Like catch → in java, except → in python
#     print("File nhi mila mere bacche!")
# finally:
#     file.close()

#file opening method 2
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')

#----------------------------------------------error handling end-----------------------------------------------------------------

#---------------------------------------match-case statement / switch-case statement start------------------------------------------
choice = input("Enter a number (1-3): ")
match choice: #just like (switch → Javascript), (match → python)
    case '1': #see carefully here, we write '1' NOT 1 (bcz, input is str NOT int)
        print("you pressed 1")
    case '2':
        print("you pressed 2")
    case '3':
        print("you pressed 3")
    case _:
        print("MKB Aaaaag! Invalid Input") #else case 
#-----------------------------------------------------match-case statement end-------------------------------------------------------

#--------------------------------------------------------------NOTES Start--------------------------------------------------------
#NOTE: to shift indentation of multiple line → select all lines → press ctrl + ] (to shift right) → ctrl + [ (to shift left)
#NOTE: dunder → underscore_underscore_name_underscore_underscore (__anyName__) → is called dunder
#NOTE: main(): → main function in python, from where the programs actually start its execution (you can't write main_func(): or final(): ALWAYS main(): , its fixed

#-------------------------------------------------------------Notes end------------------------------------------------------------
#Assignment: JSON python gfg
#----------------------------------------------------------del VS remove start------------------------------------------------------
# del → removes by index | error → IndexError
numbers = [10, 20, 30, 40]
del numbers[1] 
print(numbers)   # [10, 30, 40]

# list.remove() → removes by value | error → ValueError
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)   # [10, 30, 20] 
#----------------------------------------------------------del VS remove end------------------------------------------------------
