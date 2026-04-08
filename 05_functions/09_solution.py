#my approach
#partially correct
def even_yielder(initial, final):
    result = []
    for i in range (initial, final + 1):
        if (i % 2) == 0:
            result.append(i) 
    return result
print(even_yielder(3, 10))

#Sir approach
def even_generator(limit):
    for i in range(2, limit + 1, 2): #start → 2, upto → limit + 2, increment → 1 (bczz.. 2 means 1)
        yield i     #yield = return without exit

for num in even_generator(10):
    print(num)


#NOTE: yield use to return that value without exiting from the loop (work is just like return)
#yield VS return : return → return and exit loop, yield → return BUT does NOT exit the loop.
