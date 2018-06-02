from math import sqrt
def quadratic(a,b,c):
    d = b**2 - 4*a*c
    if(d>0):
        return ((-b+sqrt(d))/(2*a) , (-b-sqrt(d))/(2*a))
    if(d==0):
        return (-b/(2*a),)
    if(d<0):
        first = complex(-b,sqrt(-d))
        second = first.conjugate()
        return (first/(2*a),second/(2*a))

def polynomialEval(x,coeff):
    if(not coeff):return -1
    last = len(coeff)-1
    sum = 0
    for i in range(len(coeff)):
        sum+=coeff[i]*(x**last)
        last-=1
    return sum

def pig_latin(word):
    vowels = 'aeiou'
    if(word[0] in vowels):
        return word+'hay'
    elif(word[0]=='q'):
        return word[2:]+word[0:2]+'ay'
    else:
        i = 0
        temp = ''
        for letter in word:
            if(letter in vowels):
                word = word[i:]+word[0:i]
                break
            i+=1
        return word + 'ay'

def count_words(string):
    words = list(string.split())
    table_words = {}
    i=0
    for word in words:
        if(word in list(table_words.keys())):
            table_words[word].append(i)
        else:
            table_words[word] = [i]
        i+=1
    return table_words


def question1():
    setOfMultiples = set()
    for i in range(2000,3201):
        if i%7==0 and i%5!=0:
            setOfMultiples.add(i)
    return setOfMultiples
def question2(n):
    ans =1
    for i in range(1,n+1):
        ans*=i
    print(ans)

def question3(n):
    print ({i:i*i for i in range(1,n+1)})

def question4():
    print ((map(int, input().split(','))))
def question5():
    class Question5():

        def __init__(self):
            self.content=""
        def getString(this):
            this.content = str(input())
        def printString(this):
            print(this.content)

    return Question5()


def question6():
    c,h= 50,30
