#my approach
#-----------------------------Failed--------------------------------------------------
# num = 89445455
# for i in range (2, num):
#     if (num%i) == 0:
#         print(num, "is a Composite Number")
#         break
#     else:
#         print(num, "is a Prime Number")
#         break

#Sir Approach
number = 28
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)


#NOTE: for loop  ← break targets THIS
        # └── if block
        #     └── break
# break climbs up until it finds a loop, then exits it.
# for i in range(2, number):   # ← loop
#     if (number % i) == 0:    # ← condition inside loop
#         is_prime = False
#         break                # ← exits the LOOP, not the if
    