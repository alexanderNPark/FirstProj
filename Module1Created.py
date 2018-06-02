def bubbleSort(list1):
    i,swapped=0,True;
    while (swapped):
        swapped = False;
        index = i;
        for j in range(i, len(list1)):
            if (list1[index] < list1[j]):
                swapped = True;
                list1[j],list1[index] = list1[index],list1[j];
        i=i+1;
    return

def optionalFunctionParam(i=8,password="hello",user ="go",hate=True):
    if(hate):
        return password+str(i);
    else: return password+" "+user;


def selectionSort(list1):
    i,swapped = 0,False;
    while(i<len(list1)):
        swapped=False;
        index = i;
        for j in range(i+1,len(list1)):
            if(list1[index]<list1[j]):
                swapped = True;
                index=j;
        if(swapped):
            list1[i],list1[index]=list1[index],list1[i];

        i=i+1;
    return

def fibonnacci(n):
    a,b=0,1;
    listFib=[];
    for i in range(n):
        listFib.append(a);
        #listFib.append(b);
        a,b=b,a+b;
    return listFib

def addTwoNumbers(n,y):
    if y != 0:
        b = n^y
        y= (n&y)<<1
        return addTwoNumbers(b,y)
    elif y==0:
        return n
    elif n==0:
        return y

def negate(n):
    return ~n+1

def addressOf(n):
    print (hex(id(n)))
    return

def promptNumber():
    success=False
    a=0;
    while(success is not True):
        try:
            a = input("Input a number:\n");
            print(hex(id(a)));
            a=int(a);
            print(hex(id(a)));
            success=True
        except: continue

    return a;

def address(n):
    return (hex(id(n)))

def randomListOfInts(start=0,finish=100,length=50):
    from random import randint
    return [randint(start,finish) for i in range(length)]

class cheapInt(int):

    def __add__(self, other):
        return int(other*2)

    def __sub__(self, other):
        return int(other*other+4)
    def __eq__(self, other):
        int(other-self*5)
    def __and__(self,other):
        return int(other*3)

#int = cheapInt

class Node(object):
    def __lt__(self, other):
        if (self.id < other.id):
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)

numbers=[]
def initialize():
    global numbers
    numbers.clear()
    from random import randint
    for i in range(0, 25):
        n = Node()
        n.id = randint(0, 1000)
        n.data = i
        numbers.append(n)


def insertionSort(n=-1):
    if(n==-1):
        global numbers
    else:
        numbers = n
    for j in range(1, len(numbers)):
        for i in range(0, j):
            if (numbers[j] < numbers[i]):
                numbers.insert(i, numbers.pop(j))

def binarySearch(value, n=-1):
    if(n==-1):
        global numbers
    else:
        numbers = n
    def binarySearchRun(start, stop):
        if(start>stop):return -1
        midpoint = (start+stop)//2
        compare = numbers[midpoint]
        if(value==compare): return compare
        elif(value<compare): return binarySearchRun(start,midpoint-1)
        else:
            return binarySearchRun(midpoint+1,stop)
    return binarySearchRun(0,len(numbers)-1)


def quicksort(array, start, end):
    if(start>=end):
        return
    pivot_element = array[start]
    low,high = start+1,end
    while(low<=high):
        while(low<=high and array[low]<pivot_element):
            low+=1
        while(low<=high and array[high]>=pivot_element):
            high-=1
        if(low<=high):
            print("high", array[high], "at", high)
            print("low", array[low], "at", low)
            array[low],array[high] = array[high],array[low]
            low+=1
            high-=1
            print(array)

    array[start],array[high] = array[high],array[start]
    quicksort(array,start,high)
    quicksort(array,low,end)
    print(array)



"""
import random
s = [random.randint(1,1000) for i in range(10)]
#print(s)
quicksort([85,89],0,1)
#print(s)
"""

class QuickUnion:


    def __init__(self,content):
        size = max(content)+1
        self.ids = [None for _ in range(size)]
        for i in content:
            self.ids[i]=i

    def is_connected(self,first,second):


        return self.head_parent_of(first) == self.head_parent_of(second)


    def head_parent_of(self,element):
        while (self.ids[element] != element):
            element = self.ids[element]
        return element


    def union_join(self,first,second):
        self.ids[self.head_parent_of(first)] = self.head_parent_of(second)

import random
s = [i for i in range(50)]
q = QuickUnion(s)
q.union_join(5,1)
q.union_join(2,1)
q.union_join(2,4)
q.union_join(10,5)
q.union_join(9,10)
q.union_join(6,10)
print(q.is_connected(4,5))
print(q.is_connected(10,4))









