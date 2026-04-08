#Lec 6 : Python Data Types - Big Picture

username = "Aryan" #str
username= "Erazer" #OK ; Note that new memory for new str, not the previous value is updated 
# username[0] = "Z" #Not OK (str is immutable)
print(username)
print(username[0:3]) #3 not included

# dir(username.'press_here_ctrl+spacebar') #you can view all the available functions/methods for 'username' (str) with the help of suggestion (ctrl + spacebar)
#one more method to do the previous task (line: 7) is via terminal : 1. go to terminal 2. python 3. >>> username = "Aryan"
# >>> dir (username)
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']    

my_list = [123, 3.14, "chai"] #a list
print(my_list[1])

my_dict = {'Apex Predatator' : 'Rehman Dakait', 'The Jinn' : 'SP Choudhary Aslam', 'Wrath of God' : 'Jaskirat Singh Rangi', 'Bade Sahab' : None} #a dictionary
# print(my_dict[2]) #KeyError
print(my_dict['Wrath of God'])

my_tup = (1, 2, 3)
print (my_tup[1])

aStr = "AryanDev"
bStr = aStr
print(aStr)
print(bStr)
aStr = "Arya"
print(bStr) #Read after you executed in mind: Bczz bStr still pointing the reference of aStr reference (which is initially created)


#-----------------------------------------------------------------------------------
#Lecture: 7
#In draws
#--------------------------------------------------------------------------------