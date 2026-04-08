#Lec 13: Solve 10 conditional problem in python
# Github Repo : https://github.com/hiteshchoudhary/chai-aur-python/


#My Approach ↓
def classify_age(age):
    if age < 0:
        return ("Invalid Age")
    elif 0 <= age < 13:
        return ("Child")
    elif 13 <= age <= 19:
        return ("Teen")
    elif 20 <= age <= 59:
        return ("Adult")
    elif 60 <= age:
        return ("Senior")
    else:
        return ("MKB Aaaaag!")

print(classify_age(-9)) #inv
print(classify_age(0)) #child
print(classify_age(13)) #teen
print(classify_age(19)) #teen
print(classify_age(20)) #ad
print(classify_age(59)) #ad
print(classify_age(60)) #se
print(classify_age(600)) #se

#Sir Approach ↓
age = 65

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")