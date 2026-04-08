#Lec 11: Dictionary in Python

chai_dict = {'Masala' : 'Spicy', 'Green' : 'Mild', 'Ginger' : 'Zesty'} 
# print(chai_dict['Ginger']) #Method 1
# print(chai_dict.get("Ginger")) #Method 2
#Difference in Method : 1 and Method 2?
# chai_dict["wrong_argument"] #error occurs
# chai_dict.get("wrong_argument") #error NOT occurs

#print key and value from a dict
# for i, j in chai_dict.items():  #if using two loop variable "key (i), value(j)" use .items() with dict_name
#     print(i, j) #key value stored in i, value value stored in j

# chai_dict["Earl Grey"] = "Citrus" #appending an item in dictionary
# print(chai_dict)
# chai_dict.pop("Green") #you must pass argument as any key of the dictionary | Deleting Method : 1
# chai_dict.popitem() #last added item will be deleted. | Deleting Method : 2
# print(chai_dict)
# del chai_dict["Ginger"] #This del also delete the reference from the memory | Deleting Method : 3
# print(chai_dict)

#------------------------------------Nested Dict--------------------------------------
chai_dict_nested = {
    "chai" : {"Masala" : "Spicy", 'Ginger' : 'Zesty'},
    'tea' : {'Black' : 'Strong', 'Green' : 'Mild'}
}
print(chai_dict_nested['chai']['Masala']) #accesing vlaue of nested dict

squared_num_dict = {x : x**2 for x in range(10)} #square number using dict
print(squared_num_dict)
# squared_num_dict.clear() #clear the whole dictionary.

#----------------------------Creating dictionary from a given list-----------------
keys = ["Masala", "Black", "Lemon", "Oolong"]
default_value = "Delicious"
list_to_dict = dict.fromkeys(keys, default_value)
print(list_to_dict)