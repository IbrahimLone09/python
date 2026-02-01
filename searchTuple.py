"""Program to find NUMBER  
in tuple using
        WHILE LOOP """

tup = (1,4,9,16,25,36,49,64,81,100) 

x = int(input("Enter the number you want to search:"))
i = 0
while i < len(tup):
    if(tup[i] == x):
       print("Found at idx:",i)
    i= i + 1


