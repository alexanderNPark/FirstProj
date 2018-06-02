from Module1Created import *

g = 9
addressOfG = address(g)
h = 9
addressOfH = address(h)

if(addressOfH==addressOfG):
    print("true")
else:
    print ("false")

g = 9+8
addressOfGAfter = address(g) # address of G is supposed to not change if it reuses the same memory space
if(addressOfG==addressOfGAfter):
    print ("true");
else:
    print ("false");


a = "hello"
aStringAddress = address(a)
b="hello"
bStringAddress = address(b)
if(bStringAddress==aStringAddress): # if these two addresses have the same ID then they are reusing memory space pointing to the same string
    print ("true");
else:
    print ("false");

print ("a""b") # ab
print ("a"
       "b"
       'c')
num1 = 9
num1 +=9
print(a+str(num1))
print(num1)

addressOf([1,0,1][0:2])
addressOf([1,0,1][0:2])