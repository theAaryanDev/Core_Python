#my approach
#Partially correct
def factorial(n):
    result = 1
    for i in range (n,0,-1): #NOTE: range(5,0,-1) → revese a range, list[5:0:-1] → reverse a list
        result = result * i

    print(result)

factorial(5)

#Sir approach
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  #calling function inside function → rcursion

#NOTE: Recursion → calling a function inside that self function.