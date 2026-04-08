#my approach
#no idea

#sir approach
def print_kwargs(**kwargs): #** to handle unlimited key, value pairs.
    for key, value in kwargs.items(): #looping and depackaging
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")
print_kwargs(wrath_of_god="Jaskirat Singh Rangi", apex_predator="Rehman Dakait", angel_of_god = "Major Iqbal", the_jinn = "SP Aslam")