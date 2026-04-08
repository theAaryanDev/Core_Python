#My approach
#failed with multiple attempts

# def calculate_sum():
#     numbers = []
#     total_sum = 0
#     while True:
#         input_num = int(input("Enter the Number: "))
#         numbers.append(input_num)
#         for i in numbers:
#             # total_sum = total_sum + i
#             total_sum = total_sum + input_num
#         break_response = input("Do you want to exit loop: ")
#         if (break_response == 'y' or break_response == 'Y' or break_response == 'Yes' or break_response == 'yes' or break_response == 'YES'):
#             return f"Total sum is: {total_sum}"
#             # break
        
# print(calculate_sum())

# #Sir approach

def sum_all(*args): #* is MUST (args can be superman BUT args is preferred)
    print(args)
    for i in args:
        print(i * 2, end=" ")
    return sum(args) #sum → built-in function

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))