#This is a program to print fibonacci numbers.
#Designed by AnirudhCB


inp = input("How many fibonacci numbers would you like?")
x,y  = 0,1

for i in range (int (inp)):
    print (y)
    x,y = y, x+y
    
    
inp1 = input("Till what number would you like to print the fibonacci series?")
i = 1
x1,y1 = 0,1
while i<inp1: 
    print (y1)
    x1,y1 = y1, x1+y1
    i = y1

