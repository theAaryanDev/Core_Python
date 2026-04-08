#My approach Only (there is no sir approach in this)
species = "Dog"
# species = "Cat"
age = int(input("Enter the Pet's age: "))

if ((species == "Dog") and (age < 2)):
    print("Food type: Puppy food")
elif ((species == "Cat") and (age > 5)):
    print("Food type: Senior Cat Food")