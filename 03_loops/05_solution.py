#my approach
#-----------------------------------------------Failed--------------------------------
given_str = "teetereeeeeeeeeeeey"

for i in given_str:
    for j in given_str:
        if (i == j):
            continue
    
print(i, end="")           

#Sir approach
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1: #logic
        print("Char is: ", char)
        break #optimization