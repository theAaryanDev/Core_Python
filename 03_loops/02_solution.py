#My approach
n = 5
sum_of_even_number = n * (n + 1)
print(sum_of_even_number)

#Sir approach
#this is wrong, it is giving count of even no. NOT sum()
n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)