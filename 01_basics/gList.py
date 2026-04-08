#Lec 10: List in Python

tea_variety = ["Masala", "Ginger", "Green", "Black", "White", "Lemon", "Oolong"]

# print(tea_variety[:])
# print(tea_variety[-3:])
# print(tea_variety[:-3])
# print(tea_variety[2:-2])
# print(tea_variety[-4:-3])
# print(tea_variety[::-1])
# print(tea_variety[:-2:-1])

# tea_variety[1:2] = "Herbel"   #Warning: Herebal will not be treated as string (Herbal) instead it will be trated and stored like an array ('H', 'e', 'r', 'b', 'b', 'a', 'l')    here is  fix ↓
tea_variety[1:2] = ["Herbel"] #fix , this way you can replace multiple items at once ["Herbal", "Masala", "Coffee"]
print(tea_variety)

# tea_variety[1] = "Coffee" #Coffee replaces Herbal
# print(tea_variety)

tea_variety[2:2] = ["Coffee", "cold Coffee"] #Multiple items are added and also without replacing any element (updation in the middle of a list)
print(tea_variety)

tea_variety[1:3] = [] #you are inseting 'nothing' in index 1-3 (i.e nothing but deleting those elements)
print(tea_variety)

tea_variety.append("Biscuit") #add at the end of the list.
print(tea_variety)
tea_variety.pop() #removes last element
print(tea_variety)
tea_variety.remove("cold Coffee") #remove a particular elemet
print(tea_variety)

tea_variety_copy = tea_variety # same reference for both (changes in one reflects other)
tea_variety_copy = tea_variety.copy() #Seperate Reference: New memory for tea_variety_copy is created. (ant changes in tea_variety does not reflect in  tea_variety_copy)

squared_num = [x**2 for x in range(10)]
cube_num = [x**3 for x in range(10)]
print(squared_num)
print(cube_num)

list_1 = ["item 1", "item 2"]
list_2 = ["item3", "item_4"]
both_list = list_1 + list_2 #allowed
print(both_list)