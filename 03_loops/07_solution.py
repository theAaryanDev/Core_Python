#My Approach
#------------------------------Failed----------------------------------------
# input_num = 3
# def input_function():
#     input_num = int(input("Enter: "))

# while (1 < input_num < 10):
#     input_function()

#Sir Approach
while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")