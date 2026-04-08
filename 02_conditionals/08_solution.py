#My approach
password = input("Enter your Password: ")
if (len(password)<6):
    strength = "Weak"
elif (len(password) <= 10):
    strength = "Medium"
elif (len(password) > 10):
    strength = "Strong"
else:
    print("Faaaaaaaah!")

print("Your Password Strength is", strength)

#Sir approach
password = "Secure3P@ss"
password_length = len(password)

if password_length < 6:
    strength = "Weak"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)