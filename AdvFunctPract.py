from Module1Created import *
val = 5;
def listPrivate(element,lis=[]):
    lis.append(element);
    return lis;
def intPrivate(var,int=val):
    global val;
    val+=var;
    int+=val;
    return int;
def testFunction(n):
    print (n)
    return;
def test(num,bool,text1="",text2=""):
    print (str(num)+text1+text2);
    return bool
def infiniteArgFunction(*lists,**TypesAndVals):
    for i in lists:
        print(i);
    for i in TypesAndVals:
        print(str(i)+":"+str(TypesAndVals[i]));
    return;
def lambdaExpFunc(n=0):
    return lambda d:d+n*d
#listTest = randomListOfInts(0,9000,3000);
#bubbleSort(listTest);
print(listPrivate("hello"));
print(listPrivate(5));
print(listPrivate(3,[]));
print(listPrivate(True));

print(intPrivate(4));
print(intPrivate(3));
print(intPrivate(int=9,var=5));
print(optionalFunctionParam(i=8,user="ty",hate=True))
print("\n");
print(test("h","g"));

infiniteArgFunction("hello","goodbye","nice one",lol="laugh out loud",lmao="laughing my ass off");

testFunction.__call__(100000);
g=testFunction;
g(5);

directLambdaVar = lambda x: x**x;
print (directLambdaVar(4))
print("\n");
g = lambdaExpFunc(50);
print(g(1))
print(g(10));
print(lambdaExpFunc(10)(20))
#print(listTest)
#from random import randint
#print([1 for i in range(10)])
#print (fibonnacci(10));


