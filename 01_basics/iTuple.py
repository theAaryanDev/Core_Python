#Lec 12 : Tuple in Python

chai_tuple = ("Masala","Ginger", "Lemon", "Black")
# chai_tuple[2] = "Oolong" #error | disallow
chai_tuple = ("Coffee", "Cold Coffee") #allow ; no error
print(chai_tuple)

biscuit_tuple = ("Parle- G", "Marie", "Dream Lite")
all_tuple = chai_tuple + biscuit_tuple #allow 
print(all_tuple)

chai_tuple.count("Masala") #returns count of masala in tuple

(var1, var2, var3, var4, var5) = all_tuple #unpacking tuple: assigning every item of a tuple in a var in respective order. (No. of items = No. of assigned variable)
print(var1) #coffee
print(var2) #cold coffee
print(var3) #parle-g
print(var4) #marie
print(var5) #dream lite

#press comma + space simultaneously to give auto ", " after a number like (1, 2, 3, 4, 5, 6)