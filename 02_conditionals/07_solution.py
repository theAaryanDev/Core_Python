#My approach
coffee_type_dict = {1 : "Hot Coffee", 2 : "Cold Coffee", 3 : "Black Coffee"}
glass_size_dict = {1 : "Small", 2 : "Medium", 3 : "Large"}
coffee_type = int(input("Select any one type (1/2/3): \n1: Hot Coffee \n 2: Cold Coffee \n 3: Black Coffee \n"))
glass_size = int(input("Select Glass Size (1/2/3): \n 1: Small \n 2: Medium \n 3: Large\n"))
add_on_input = input("would you like to add Extra Shot of espresso? \n Y for Yes & N for No\n")
add_on_lowered = add_on_input.lower()

if (add_on_lowered == 'y'):
    order = f"Your order deatils are: \n Coffee Type : {coffee_type_dict[coffee_type]} \n Quantity : {glass_size_dict[coffee_type]} \n with extra shot of espresso"
elif (add_on_lowered == 'n'):
    order = f"Your order deatils are: \n Coffee Type : {coffee_type_dict[coffee_type]} \n Quantity : {glass_size_dict[coffee_type]}"

print(order)

#Sir approach
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)