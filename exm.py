def isEven(n) :
    return (n & 1);

n = int(input("Enter a number : "))
if(isEven(n) == 0):
    print ("Even")
else :
    print ("Odd")

