#My approach
# password= 1234
# entered_password = None
# password_is_false = True
# retries = 0
# wait_time = 1
# while password_is_false:
#     entered_password = int(input("Enter Pass: "))
#     if entered_password == password:
#         print("Welcome, You logged in")
#         password_is_false = False
#         break
#     else:
#         retries += 1
#         wait_time *= 2
#         print("Your wait time is: ", wait_time, "Seconds")
        
#Sir Approach
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1