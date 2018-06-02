from collections import deque
def p(self,element):
    self.queue.append(element)
    return
class FirstClass:
    staticI = 0
    appendToQueue = p

    def __init__(self,name,religion,age,**extra):
        self.age=age
        self.religion=religion
        self.name=name
        self.queue = deque([]);
        FirstClass.staticI=9

    def setAttributes(self,*args):
        self.attributes=args

    def printAttributes(self):
        print(self.attributes)

    def firstFunc(self,newI,imprint):
        FirstClass.i = newI
        self.imprint = imprint

    def toString(self):
        print(self.name,self.religion,self.age,FirstClass.staticI)

class SecondClass(FirstClass):

    def __init__(self,name,age,religion, **extraForSuperClass):
        super().__init__(name,age,religion,**extraForSuperClass)

    def printAttributes(self):
        print(self.attributes.__dict__);


class ThirdClass(SecondClass):
    def __init__(self,date,name,religion1,religion2,age,**extraForSuperClass):
        super().__init__(name+date+religion1+religion2,age,**extraForSuperClass)
        print ("class created",name+date,age,religion1+religion2)

class FourthClass(ThirdClass,SecondClass):
    def __init__(self):
        defaultKeys = {"name":"Alex", "date":"December", "age":17, "religion":"Christian","religion1":"Hell", "religion2":"Heaven"}
        super().__init__(**defaultKeys)

    def __str__(self):
        print(self.name,self.religion1)



FourthClass()









