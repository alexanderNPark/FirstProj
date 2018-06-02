from collections import deque
def problem1():
    strToAnalyze = list(""" map """)
    i=0
    print(strToAnalyze)
    for char in strToAnalyze:
        if(ord(char)>=97 and ord(char)<=122):
            if(char=='y'):
                strToAnalyze[i] = "a"
            elif(char=='z'):
                strToAnalyze[i] = "b"
            else: strToAnalyze[i] = chr(ord(char)+2)
        i=i+1
    print ("".join(strToAnalyze))

def problem2():
    fileName = r"c:\pyCharm_WS\first\problem2.html";
    file = open(fileName, 'r');
    list1 =[]
    for line in file:
        for char in line:
            if (ord(char)<=90 and ord(char)>=65) or ((ord(char)<=122 and ord(char)>=97)):
                list1.append(char)
    print("".join(list1))


def hanoi(n, a,b,c):
    if(n==1):
        print("TOP DISK MOVED",a,"TO",c)
        return
    hanoi(n-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(n-1, b,a,c)

def stringBinary(n):
    if(n==0):return ""
    return stringBinary(n//2)+str(n%2)

def sumateRecursively(n,function):
    if(n==0):return 0
    else: return function(n)+sumateRecursively(n-1,function)

def isPalindrome(string):
    if(string==None or len(string)==0):
        return True
    if(string[0]!=string[len(string)-1]):
        return False
    return isPalindrome(string[1:(len(string)-1) ])

def hexadecimal(n):
    i = n%16
    if(n==0):return ""
    if(i>9):i = str(chr(i+55))
    else: i = str(i)
    return hexadecimal(n//16)+i


def fibonacciRecur(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRecur(n-1) + fibonacciRecur(n-2)

def permutation(word):
    count =0
    def permutate(new,old):
        nonlocal count
        if(len(old) == 0 or old == None):
            count+=1
            print(new);
        else:
            for i in old:
                permutate(new+str(i), old.replace(i,""))
    permutate("",word)
    print(count)

def gcd(a,b):
    return b if a % b == 0 else gcd(b, a % b)


def hotPotatoQueue(n=5):
    queueNames = deque([])
    while len(queueNames) < n:
        queueNames.append(input("Enter a Name in order:\n").lower())
    i,a = 0,int(input("Number of Passes"))
    firstName = input("Name of starter").lower()
    if(firstName in queueNames):
        for g in range(0,queueNames.index(firstName)+a):
            queueNames.append(queueNames.popleft())
        return queueNames.popleft()
    else:
        print("Need a starter")
        return



pegs = [chr(x) for x in range(65,69)]
hanoi(4,pegs[0],pegs[1],pegs[2])
f = lambda x,y=0: 2**(x-y)
print(sumateRecursively(3,f))
print(hexadecimal(956))
print(fibonacciRecur(6))
#permutation("abcd")
gcd_vals = [45,136]
print(gcd(*gcd_vals))
gcd_vals[2:3]=[89]
print(*gcd_vals)
print(hotPotatoQueue())



